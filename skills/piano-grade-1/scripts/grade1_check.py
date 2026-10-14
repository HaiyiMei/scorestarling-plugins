#!/usr/bin/env python3
"""Check a two-hand piano MusicXML score against the Grade 1 profile in ../references/grade-1.md.

Usage: python3 grade1_check.py score.musicxml [--json] [--mark marked.musicxml]

Prints one line per check (ok / warn / over) with bar numbers, then a verdict. --mark writes a
copy with every note that broke a check coloured red, for a before/after picture. Standard library
only; reads .musicxml, .xml and .mxl. It measures notation, not musicianship: a clean result does
not prove the melody survived or that the piece sounds good, so listen and compare as well.
"""
import argparse
import json
import sys
import xml.etree.ElementTree as ET
import zipfile
from collections import defaultdict
from fractions import Fraction

STEPS = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
SHORT_TYPES = {'16th', '32nd', '64th', '128th'}
RED = '#D0021B'


def load(path):
    if path.endswith('.mxl'):
        with zipfile.ZipFile(path) as z:
            names = [n for n in z.namelist() if not n.startswith('META-INF') and n.endswith(('.xml', '.musicxml'))]
            return ET.ElementTree(ET.fromstring(z.read(names[0])))
    return ET.parse(path)


def text(el, path, default=None):
    found = el.find(path)
    return found.text.strip() if found is not None and found.text else default


class Note:
    def __init__(self, el, bar, onset, dur, hand, voice):
        self.el, self.bar, self.onset, self.dur, self.hand, self.voice = el, bar, onset, dur, hand, voice
        pitch = el.find('pitch')
        self.midi = None
        if pitch is not None:
            self.midi = (int(text(pitch, 'octave')) + 1) * 12 + STEPS[text(pitch, 'step')] + int(float(text(pitch, 'alter', '0')))
            self.alter = int(float(text(pitch, 'alter', '0')))
            self.step = text(pitch, 'step')
        self.type = text(el, 'type')
        self.dots = len(el.findall('dot'))
        self.tuplet = el.find('time-modification') is not None
        self.grace = el.find('grace') is not None
        self.tied_from = any(t.get('type') == 'stop' for t in el.findall('tie'))


def read_score(tree):
    root = tree.getroot()
    parts = root.findall('part')
    notes, info = [], {'keys': [], 'times': [], 'clef_changes': [], 'pedal': [], 'octave_shift': [], 'tempo': [], 'bars': 0}
    two_parts = len(parts) >= 2 and all(p.find('measure/attributes/staves') is None for p in parts[:2])
    for p_index, part in enumerate(parts[:2] if two_parts else parts[:1]):
        divisions = 1
        bar_count = 0
        clefs_seen = {}
        start = Fraction(0)
        for m_index, measure in enumerate(part.findall('measure')):
            bar = m_index + 1
            bar_count = bar
            pos = Fraction(0)
            longest = Fraction(0)
            last_onset = Fraction(0)
            for el in measure:
                if el.tag == 'attributes':
                    divisions = int(text(el, 'divisions', divisions))
                    for key in el.findall('key'):
                        if p_index == 0:
                            info['keys'].append((bar, int(text(key, 'fifths', '0')), text(key, 'mode', 'major')))
                    for time in el.findall('time'):
                        if p_index == 0:
                            info['times'].append((bar, f"{text(time, 'beats')}/{text(time, 'beat-type')}"))
                    for clef in el.findall('clef'):
                        staff = clef.get('number', str(p_index + 1))
                        sign = text(clef, 'sign')
                        if staff in clefs_seen and clefs_seen[staff] != sign:
                            info['clef_changes'].append(bar)
                        clefs_seen[staff] = sign
                elif el.tag == 'direction':
                    if el.find('direction-type/pedal') is not None:
                        info['pedal'].append(bar)
                    shift = el.find('direction-type/octave-shift')
                    if shift is not None and shift.get('type') != 'stop':
                        info['octave_shift'].append(bar)
                    sound = el.find('sound')
                    if sound is not None and sound.get('tempo'):
                        info['tempo'].append((bar, float(sound.get('tempo'))))
                elif el.tag == 'backup':
                    pos -= Fraction(int(text(el, 'duration', '0')), divisions)
                elif el.tag == 'forward':
                    pos += Fraction(int(text(el, 'duration', '0')), divisions)
                elif el.tag == 'note':
                    dur = Fraction(int(text(el, 'duration', '0')), divisions)
                    chord = el.find('chord') is not None
                    onset = last_onset if chord else pos
                    staff = text(el, 'staff', '1')
                    hand = ('RH' if p_index == 0 else 'LH') if two_parts else ('RH' if staff == '1' else 'LH')
                    if el.find('rest') is None:
                        note = Note(el, bar, (bar, onset), dur, hand, text(el, 'voice', '1'))
                        note.time = start + onset
                        notes.append(note)
                    if not chord:
                        last_onset = pos
                        pos += dur
                longest = max(longest, pos)
            start += longest
        info['bars'] = max(info['bars'], bar_count)
    return notes, info


def five_finger_shifts(seq):
    """Greedy count of new hand positions: a position covers a fifth (7 semitones)."""
    shifts, lo, hi, where = 0, None, None, []
    for n in seq:
        if lo is None:
            lo = hi = n.midi
            continue
        new_lo, new_hi = min(lo, n.midi), max(hi, n.midi)
        if new_hi - new_lo > 7:
            shifts += 1
            where.append(n.bar)
            lo = hi = n.midi
        else:
            lo, hi = new_lo, new_hi
    return shifts, where


def check(notes, info):
    results = []
    flagged = set()

    def add(name, status, detail, bad=()):
        results.append({'check': name, 'status': status, 'detail': detail})
        for n in bad:
            flagged.add(id(n.el))

    bars = info['bars']
    # Key
    keys = info['keys'] or [(1, 0, 'major')]
    fifths = keys[0][1]
    key_status = 'ok' if abs(fifths) <= 1 else ('warn' if abs(fifths) == 2 else 'over')
    add('key', key_status, f'{abs(fifths)} {"sharp" if fifths > 0 else "flat"}{"s" if abs(fifths) != 1 else ""} '
        f'({keys[0][2]}); Grade 1 keys use at most one' if fifths else f'no sharps or flats ({keys[0][2]})')
    if len({k[1] for k in keys}) > 1:
        add('key changes', 'warn', 'key changes at bars ' + ', '.join(str(k[0]) for k in keys[1:]))
    # Time
    times = info['times'] or [(1, '4/4')]
    t0 = times[0][1]
    add('time signature', 'ok' if t0 in ('2/4', '3/4', '4/4') else ('warn' if t0 in ('3/8', '6/8', '2/2') else 'over'), t0)
    if len({t[1] for t in times}) > 1:
        add('time changes', 'warn', 'meter changes at bars ' + ', '.join(str(t[0]) for t in times[1:]))
    # Length
    add('length', 'ok' if 8 <= bars <= 40 else 'warn', f'{bars} bars (Grade 1 pieces are usually 8–40)')
    # Rhythm
    short = [n for n in notes if n.type in SHORT_TYPES or (n.type == 'eighth' and n.dots)]
    add('shortest notes', 'over' if short else 'ok',
        f'{len(short)} notes shorter than an eighth (or dotted eighths), bars {bars_of(short)}' if short else 'eighths or longer', short)
    tup = [n for n in notes if n.tuplet]
    if tup:
        add('tuplets', 'over', f'{len(tup)} tuplet notes, bars {bars_of(tup)}', tup)
    grace = [n for n in notes if n.grace]
    if grace:
        add('grace notes', 'over', f'{len(grace)} grace notes, bars {bars_of(grace)}', grace)
    # Per hand
    for hand in ('RH', 'LH'):
        hn = [n for n in notes if n.hand == hand and not n.grace]
        if not hn:
            add(f'{hand} present', 'warn', f'no {hand} notes')
            continue
        by_onset = defaultdict(list)
        for n in hn:
            by_onset[n.onset].append(n)
        onsets = sorted(by_onset)
        stacks = [by_onset[o] for o in onsets]
        # Notes at once (struck together, ties excluded)
        struck = [[n for n in s if not n.tied_from] for s in stacks]
        three = [s for s in struck if len(s) >= 3]
        two = [s for s in struck if len(s) == 2]
        share = len(two) / max(1, len(stacks))
        if three:
            add(f'{hand} notes at once', 'over', f'{len(three)} chords of 3+ notes, bars {bars_of([s[0] for s in three])}',
                [n for s in three for n in s])
        else:
            add(f'{hand} notes at once', 'ok' if share <= 0.25 else 'warn',
                f'at most 2; two-note intervals on {share:.0%} of onsets' + ('' if share <= 0.25 else ' (keep them occasional)'),
                [n for s in two for n in s] if share > 0.25 else ())
        wide = [s for s in struck if len(s) == 2 and max(n.midi for n in s) - min(n.midi for n in s) > 9]
        if wide:
            over = [s for s in wide if max(n.midi for n in s) - min(n.midi for n in s) > 12]
            add(f'{hand} stretch', 'over' if over else 'warn',
                f'{len(wide)} intervals wider than a sixth, bars {bars_of([s[0] for s in wide])}', [n for s in wide for n in s])
        # Voices inside one hand
        voices = {n.voice for n in hn}
        if len(voices) > 1:
            add(f'{hand} voices', 'warn', f'{len(voices)} voices in one hand; Grade 1 hands play one line')
        # Range and leaps (top line for RH, bottom line for LH)
        line = [max(s, key=lambda n: n.midi) if hand == 'RH' else min(s, key=lambda n: n.midi) for s in stacks]
        lo, hi = min(n.midi for n in hn), max(n.midi for n in hn)
        span = hi - lo
        add(f'{hand} range', 'ok' if span <= 19 else ('warn' if span <= 24 else 'over'),
            f'{name_of(lo)}–{name_of(hi)} ({span} semitones; up to an octave and a fifth is comfortable)')
        # A jump after a rest or a long note (half or longer) gives the hand time to move,
        # as at a phrase end or a new section, so only count jumps between connected notes.
        joined = [(a, b) for a, b in zip(line, line[1:]) if a.dur < 2 and b.time <= a.time + a.dur]
        leaps = [b for a, b in joined if abs(b.midi - a.midi) > 12]
        sixths = [b for a, b in joined if 9 < abs(b.midi - a.midi) <= 12]
        if leaps:
            add(f'{hand} leaps', 'over', f'{len(leaps)} jumps over an octave between connected notes, bars {bars_of(leaps)}', leaps)
        elif len(sixths) > max(2, bars // 8):
            add(f'{hand} leaps', 'warn', f'{len(sixths)} jumps of a seventh or octave, bars {bars_of(sixths)}', sixths)
        # Two or more ledger lines: RH below B3 or above B5; LH below D2 or above D4
        low_lim, high_lim = (59, 83) if hand == 'RH' else (38, 62)
        ledger = [n for n in hn if n.midi < low_lim or n.midi > high_lim]
        if len(ledger) > max(2, len(hn) // 20):
            add(f'{hand} ledger lines', 'warn', f'{len(ledger)} notes beyond one ledger line, bars {bars_of(ledger)}', ledger)
        # Hand positions
        shifts, where = five_finger_shifts(line)
        per8 = shifts / max(1, bars) * 8
        add(f'{hand} hand positions', 'ok' if per8 <= 6 else ('warn' if per8 <= 10 else 'over'),
            f'{shifts} moves out of a five-finger position ({per8:.1f} per 8 bars)')
        # Pace
        if hand == 'LH':
            quick = [s[0] for s in stacks if s[0].dur < 1]
            share_q = len(quick) / len(stacks)
            add('LH pace', 'ok' if share_q <= 0.3 else ('warn' if share_q <= 0.6 else 'over'),
                f'{share_q:.0%} of LH onsets are eighths; Grade 1 LH moves mostly in quarters or slower',
                quick if share_q > 0.3 else ())
    # Both hands busy in eighths together
    rh_q = {n.onset for n in notes if n.hand == 'RH' and n.dur < 1}
    lh_q = {n.onset for n in notes if n.hand == 'LH' and n.dur < 1}
    both = rh_q & lh_q
    if len(both) > max(4, bars // 2):
        add('hands together in eighths', 'warn', f'{len(both)} eighth-note onsets in both hands at once')
    # Accidentals outside the key
    scale = key_scale(fifths)
    acc = [n for n in notes if (n.midi % 12) not in scale]
    add('accidentals', 'ok' if len(acc) <= max(2, bars // 4) else 'warn', f'{len(acc)} notes outside the key signature',
        acc if len(acc) > max(2, bars // 4) else ())
    # Pedal, octave lines, clef changes, tempo
    if info['pedal']:
        add('pedal', 'warn', f'pedal marked in {len(set(info["pedal"]))} bars; Grade 1 pieces rarely need it')
    if info['octave_shift']:
        add('octave lines', 'over', f'8va/8vb at bars {", ".join(map(str, sorted(set(info["octave_shift"]))))}')
    if info['clef_changes']:
        add('clef changes', 'over', f'clef changes at bars {", ".join(map(str, sorted(set(info["clef_changes"]))))}')
    if info['tempo']:
        fast = max(t for _, t in info['tempo'])
        add('tempo', 'ok' if fast <= 132 else 'warn', f'up to {fast:g} quarter notes a minute')
    return results, flagged


def key_scale(fifths):
    tonic = (7 * fifths) % 12
    major = {(tonic + i) % 12 for i in (0, 2, 4, 5, 7, 9, 11)}
    # Allow the raised 7th of the relative minor (harmonic minor), common at Grade 1.
    return major | {(tonic + 8) % 12}


def bars_of(items):
    bars = sorted({n.bar for n in items})
    if len(bars) > 8:
        return ', '.join(map(str, bars[:8])) + f' … ({len(bars)} bars)'
    return ', '.join(map(str, bars))


def name_of(midi):
    return ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B'][midi % 12] + str(midi // 12 - 1)


def verdict(results):
    statuses = [r['status'] for r in results]
    if 'over' in statuses:
        return 'above Grade 1'
    if statuses.count('warn') > 2:
        return 'close to Grade 1, with several harder spots'
    return 'about Grade 1' if 'warn' not in statuses else 'about Grade 1, with a few harder spots'


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('score')
    parser.add_argument('--json', action='store_true', help='print JSON instead of text')
    parser.add_argument('--mark', help='write a copy with notes that broke a check coloured red')
    args = parser.parse_args()
    tree = load(args.score)
    notes, info = read_score(tree)
    if not notes:
        sys.exit('No notes found: is this a MusicXML score?')
    results, flagged = check(notes, info)
    summary = {'verdict': verdict(results), 'bars': info['bars'], 'checks': results}
    if args.mark:
        for n in notes:
            if id(n.el) in flagged:
                n.el.set('color', RED)
                for child in ('notehead', 'stem', 'beam', 'accidental'):
                    for c in n.el.findall(child):
                        c.set('color', RED)
        tree.write(args.mark, encoding='utf-8', xml_declaration=True)
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return
    for r in results:
        print(f"{r['status']:>4}  {r['check']}: {r['detail']}")
    print(f"\nVerdict: {summary['verdict']}")


if __name__ == '__main__':
    main()
