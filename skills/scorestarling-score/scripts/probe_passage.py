#!/usr/bin/env python3
"""Probe a few seconds of a recording: onsets, the notes struck at each onset, pitch classes and an optional
melody line. Every array goes to OUT/probe.json and the pictures to OUT/*.png; the screen gets a short summary.

For checking a few bars, one pitch or one onset, never for transcribing a whole recording. Needs numpy and librosa;
matplotlib for the pictures (skipped when it is missing). Never writes its input.

  python3 scripts/probe_passage.py AUDIO --start 12.0 --end 18.5 --out probe-12s
  python3 scripts/probe_passage.py AUDIO --start 12 --end 18.5 --out probe-12s --melody
"""

import argparse
import json
import sys
from pathlib import Path

MAX_SECONDS = 15.0
MAX_LINES = 40
LOWEST, BINS = 'A0', 88  # the piano's range, a bin per semitone


def notes_at(cqt, before, after, librosa, top=3, floor_db=-30.0, rise_db=6.0):
    """The semitone bins that grow most across an onset (the notes struck there, not the ones still ringing), loud
    enough to matter; the loudest bins when nothing rises. Note names."""
    column = cqt[:, after]
    loud = column >= column.max() + floor_db
    rise = column - cqt[:, before]
    struck = [b for b in rise.argsort()[::-1] if loud[b] and rise[b] >= rise_db][:top]
    if not struck:
        struck = [b for b in column.argsort()[::-1] if loud[b]][:top]
    lowest = librosa.note_to_midi(LOWEST)
    return [librosa.midi_to_note(lowest + int(b), unicode=False) for b in struck]


def probe(audio, start, end, out, melody=False):
    if not 0 <= start < end or end - start > MAX_SECONDS:
        raise SystemExit(f'Probe 0 < end - start <= {MAX_SECONDS:g} seconds; use the score tools for longer stretches')
    import librosa  # noqa: PLC0415 heavy, needed only here
    import numpy as np  # noqa: PLC0415 heavy, needed only here

    y, sr = librosa.load(audio, sr=22050, mono=True, offset=start, duration=end - start)
    if not len(y):
        raise SystemExit('No audio in that window')
    out.mkdir(parents=True, exist_ok=True)
    hop = 512
    cqt = librosa.amplitude_to_db(
        np.abs(librosa.cqt(y, sr=sr, hop_length=hop, fmin=librosa.note_to_hz(LOWEST), n_bins=BINS)), ref=np.max
    )
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop)
    onsets = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr, hop_length=hop, backtrack=False)
    times = librosa.frames_to_time(onsets, sr=sr, hop_length=hop) + start
    tempo = float(np.atleast_1d(librosa.feature.tempo(onset_envelope=onset_env, sr=sr, hop_length=hop))[0])
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr, hop_length=hop)
    names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    weight = chroma.mean(axis=1)
    # A little after each onset, once the attack noise has passed.
    lag = max(1, int(0.05 * sr / hop))
    last = cqt.shape[1] - 1
    heard = [notes_at(cqt, max(0, frame - lag), min(frame + lag, last), librosa) for frame in onsets]
    result = {
        'audio': str(audio),
        'window': {'start_seconds': start, 'end_seconds': end},
        'tempo_bpm_estimate': round(tempo, 1),
        'onsets': [{'seconds': round(float(t), 3), 'struck_notes': n} for t, n in zip(times, heard)],
        'pitch_class_weights': {names[i]: round(float(weight[i]), 3) for i in range(12)},
        'cqt_db': {'lowest': LOWEST, 'hop_seconds': hop / sr, 'values': np.round(cqt, 1).tolist()},
    }
    if melody:
        f0, voiced, _ = librosa.pyin(
            y, sr=sr, hop_length=hop, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7')
        )
        line = []
        for i, (hz, on) in enumerate(zip(f0, voiced)):
            if on and np.isfinite(hz):
                note = librosa.hz_to_note(hz, unicode=False)
                if not line or line[-1]['note'] != note:
                    line.append({'seconds': round(start + i * hop / sr, 3), 'note': note})
        result['melody'] = line
    (out / 'probe.json').write_text(json.dumps(result))
    pictures = draw(cqt, chroma, times, start, end, sr, hop, out, librosa)

    lines = [
        f'Window {start:g}-{end:g} s of {Path(audio).name}; tempo estimate {tempo:.0f} BPM; {len(times)} onsets.',
        'Strongest pitch classes: ' + ', '.join(f'{names[i]} {weight[i]:.2f}' for i in weight.argsort()[::-1][:5]),
    ]
    shown = MAX_LINES - 6
    for item in result['onsets'][:shown]:
        lines.append(f'  {item["seconds"]:8.3f} s  ' + ' '.join(item['struck_notes']))
    if len(result['onsets']) > shown:
        lines.append(f'  ... {len(result["onsets"]) - shown} more onsets in probe.json')
    if melody:
        lines.append(
            'Melody: '
            + ' '.join(n['note'] for n in result['melody'][:24])
            + (' ...' if len(result['melody']) > 24 else '')
        )
    lines.append(f'Full data: {out / "probe.json"}')
    if pictures:
        lines.append('Look at: ' + ', '.join(str(p) for p in pictures))
    print('\n'.join(lines[:MAX_LINES]))


def draw(cqt, chroma, times, start, end, sr, hop, out, librosa):
    try:
        import matplotlib  # noqa: PLC0415 optional

        matplotlib.use('Agg')
        import librosa.display  # noqa: PLC0415 needs matplotlib
        import matplotlib.pyplot as plt  # noqa: PLC0415 optional
    except ImportError:
        return []
    pictures = []
    figure, axis = plt.subplots(figsize=(12, 6))
    librosa.display.specshow(
        cqt, sr=sr, hop_length=hop, x_axis='time', y_axis='cqt_note', fmin=librosa.note_to_hz(LOWEST), ax=axis
    )
    for t in times:
        axis.axvline(t - start, color='white', linewidth=0.5, alpha=0.6)
    axis.set_title(f'Notes heard, {start:g}-{end:g} s (lines: onsets)')
    figure.tight_layout()
    figure.savefig(out / 'cqt.png', dpi=110)
    plt.close(figure)
    pictures.append(out / 'cqt.png')
    figure, axis = plt.subplots(figsize=(12, 3))
    librosa.display.specshow(chroma, sr=sr, hop_length=hop, x_axis='time', y_axis='chroma', ax=axis)
    axis.set_title('Pitch classes')
    figure.tight_layout()
    figure.savefig(out / 'chroma.png', dpi=110)
    plt.close(figure)
    pictures.append(out / 'chroma.png')
    return pictures


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('audio', type=Path)
    parser.add_argument('--start', type=float, required=True, help='seconds into the recording')
    parser.add_argument('--end', type=float, required=True, help=f'at most {MAX_SECONDS:g} seconds after start')
    parser.add_argument('--out', type=Path, required=True, help='folder for probe.json and the pictures')
    parser.add_argument('--melody', action='store_true', help='also follow one melody line (slower)')
    args = parser.parse_args(argv)
    if not args.audio.is_file():
        raise SystemExit(f'No such audio file: {args.audio}')
    probe(args.audio, args.start, args.end, args.out, args.melody)


if __name__ == '__main__':
    sys.exit(main())
