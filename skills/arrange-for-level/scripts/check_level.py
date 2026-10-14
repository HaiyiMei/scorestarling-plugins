#!/usr/bin/env python3
"""Check a MusicXML score against the level profile of an instrument and grade.

Usage:
  python3 check_level.py score.musicxml --instrument piano --grade 2 [--json] [--mark marked.musicxml]
  python3 check_level.py score.musicxml --instrument violin --estimate
  python3 check_level.py --list

Profiles live in ../references/profiles/<instrument>.json (see ../references/levels.md for where each
number comes from). Prints one line per check (ok / warn / over / info) with bar numbers, then a
verdict. --estimate runs every grade of the profile and reports the lowest one with nothing over.
--mark writes a copy with every note that broke a check coloured red, for a before/after picture.
Standard library only; reads .musicxml, .xml and .mxl. It measures notation, not musicianship: a
clean result does not prove the melody survived or that the piece sounds good, so listen and
compare as well.
"""
import argparse
import json
import sys
import xml.etree.ElementTree as ET
import zipfile
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

STEPS = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
SHORT_TYPES = {'16th', '32nd', '64th', '128th'}
TINY_TYPES = {'32nd', '64th', '128th'}
RED = '#D0021B'
PROFILES = Path(__file__).resolve().parent.parent / 'references' / 'profiles'
DEFAULT_TEMPO = 96.0


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
        self.midi = None
        pitch = el.find('pitch')
        if pitch is not None:
            self.midi = (int(text(pitch, 'octave')) + 1) * 12 + STEPS[text(pitch, 'step')] + int(float(text(pitch, 'alter', '0')))
        unpitched = el.find('unpitched')
        inst = el.find('instrument')
        self.inst = inst.get('id') if inst is not None else (
            f"{text(unpitched, 'display-step')}{text(unpitched, 'display-octave')}" if unpitched is not None else None)
        self.type = text(el, 'type')
        self.dots = len(el.findall('dot'))
        self.tuplet = el.find('time-modification') is not None
        self.grace = el.find('grace') is not None
        self.tied_from = any(t.get('type') == 'stop' for t in el.findall('tie'))


def read_score(tree, kind, part_number=1):
    root = tree.getroot()
    parts = root.findall('part')
    notes = []
    info = {'keys': [], 'times': [], 'clef_changes': [], 'pedal': [], 'octave_shift': [], 'tempo': [],
            'bars': 0, 'quarters': Fraction(0), 'parts': len(parts), 'has_transpose': False}
    if kind == 'keyboard':
        two_parts = len(parts) >= 2 and all(p.find('measure/attributes/staves') is None for p in parts[:2])
        chosen = parts[:2] if two_parts else parts[:1]
    else:
        two_parts = False
        chosen = [parts[min(part_number, len(parts)) - 1]]
    for p_index, part in enumerate(chosen):
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
                    if el.find('transpose') is not None:
                        info['has_transpose'] = True
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
                    if kind == 'keyboard':
                        hand = ('RH' if p_index == 0 else 'LH') if two_parts else ('RH' if staff == '1' else 'LH')
                    else:
                        hand = 'line'
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
        if p_index == 0:
            info['quarters'] = start
    return notes, info


# --- profiles -----------------------------------------------------------------------------------

def profile_files():
    return sorted(PROFILES.glob('*.json'))


def load_profile(name):
    wanted = name.lower().strip().replace(' ', '-')
    for path in profile_files():
        data = json.loads(path.read_text(encoding='utf-8'))
        names = [data['instrument']] + data.get('aliases', [])
        if wanted in [n.lower().replace(' ', '-') for n in names]:
            return data
    sys.exit(f'No profile for "{name}". Available: ' + ', '.join(
        json.loads(p.read_text(encoding='utf-8'))['instrument'] for p in profile_files()))


def grade_key(profile, grade):
    keys = list(profile['grades'])
    if str(grade) in keys:
        return str(grade)
    sys.exit(f'{profile["instrument"]} has no grade "{grade}". Available: ' + ', '.join(keys))


def grade_label(profile, key):
    names = profile.get('grade_names', {})
    return names.get(key) or f'{profile.get("grade_word", "Grade")} {key}'


# --- helpers ------------------------------------------------------------------------------------

def bars_of(items):
    bars = sorted({n.bar for n in items})
    if len(bars) > 8:
        return ', '.join(map(str, bars[:8])) + f' … ({len(bars)} bars)'
    return ', '.join(map(str, bars))


def name_of(midi):
    return ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B'][midi % 12] + str(midi // 12 - 1)


def key_scale(fifths):
    tonic = (7 * fifths) % 12
    major = {(tonic + i) % 12 for i in (0, 2, 4, 5, 7, 9, 11)}
    # Allow the raised 7th of the relative minor (harmonic minor), common at low grades.
    return major | {(tonic + 8) % 12}


def window_shifts(seq, window):
    """Greedy count of new hand positions: one position covers `window` semitones."""
    shifts, lo, hi, where = 0, None, None, []
    for n in seq:
        if lo is None:
            lo = hi = n.midi
            continue
        new_lo, new_hi = min(lo, n.midi), max(hi, n.midi)
        if new_hi - new_lo > window:
            shifts += 1
            where.append(n.bar)
            lo = hi = n.midi
        else:
            lo, hi = new_lo, new_hi
    return shifts, where


def fifths_for_tonic(pc):
    """Key signature (as a count of sharps, negative for flats) of the major key on pitch class pc."""
    return min((f for f in range(-6, 7) if (7 * f) % 12 == pc), key=abs)


def to_written(notes, info, offset):
    """Shift concert-pitch notes and key signatures up by `offset` semitones to written pitch."""
    for n in notes:
        if n.midi is not None:
            n.midi += offset
    info['keys'] = [(bar, fifths_for_tonic(((7 * f) + offset) % 12), mode) for bar, f, mode in info['keys']]


def tempo_of(info):
    if info['tempo']:
        return info['tempo'][0][1], False
    return DEFAULT_TEMPO, True


def runs_of(notes, gap):
    """Unbroken stretches of sound: consecutive notes with less than `gap` quarters of rest between."""
    runs, cur, end = [], [], None
    for n in sorted(notes, key=lambda n: n.time):
        if cur and n.time - end >= gap:
            runs.append(cur)
            cur, end = [], None
        cur.append(n)
        stop = n.time + n.dur
        end = stop if end is None else max(end, stop)
    if cur:
        runs.append(cur)
    return runs


# --- checks -------------------------------------------------------------------------------------

class Report:
    def __init__(self, ignore=()):
        self.results, self.flagged, self.ignore = [], set(), set(ignore)

    def add(self, name, status, detail, bad=()):
        if name in self.ignore:
            self.results.append({'check': name, 'status': 'info', 'detail': f'(ignored) {detail}'})
            return
        self.results.append({'check': name, 'status': status, 'detail': detail})
        for n in bad:
            self.flagged.add(id(n.el))


def band(value, ok_max, warn_max):
    return 'ok' if value <= ok_max else ('warn' if value <= warn_max else 'over')


def check_common(notes, info, g, next_g, rep, kind):
    bars = info['bars']
    pitched = [n for n in notes if n.midi is not None]
    # Key
    keys = info['keys'] or [(1, 0, 'major')]
    first = keys[0]
    if g.get('key_sigs') is not None and kind != 'percussion':
        allowed = set(g['key_sigs'])
        worst = 'ok'
        for _, f, _ in keys:
            if f in allowed:
                continue
            near = any(abs(f - a) == 1 for a in allowed)
            worst = 'over' if worst == 'over' or not near else 'warn'
        listed = ', '.join((f'{abs(a)} {"sharp" if a > 0 else "flat"}' + ('s' if abs(a) > 1 else '')) if a else 'none' for a in sorted(allowed))
        rep.add('key', worst, f'{abs(first[1])} {"sharp" if first[1] > 0 else "flat"}{"s" if abs(first[1]) != 1 else ""} ({first[2]})'
                if first[1] else f'no sharps or flats ({first[2]})', ())
        rep.results[-1]['detail'] += f'; key signatures this level reads: {listed}'
        if len({k[1] for k in keys}) > 1:
            rep.add('key changes', 'warn', 'key changes at bars ' + ', '.join(str(k[0]) for k in keys[1:]))
    elif g.get('key_max_acc') is not None and kind != 'percussion':
        worst = max(abs(k[1]) for k in keys)
        limit = g['key_max_acc']
        rep.add('key', 'ok' if worst <= limit else ('warn' if worst == limit + 1 else 'over'),
                f'{abs(first[1])} {"sharp" if first[1] > 0 else "flat"}{"s" if abs(first[1]) != 1 else ""} ({first[2]}); '
                f'this level uses at most {limit}' if first[1] else f'no sharps or flats ({first[2]}); this level uses at most {limit}')
        if len({k[1] for k in keys}) > 1:
            rep.add('key changes', 'warn', 'key changes at bars ' + ', '.join(str(k[0]) for k in keys[1:]))
    # Meter
    times = info['times'] or [(1, '4/4')]
    if g.get('meters'):
        status = 'ok'
        for _, t in times:
            if t in g['meters']:
                continue
            nxt = (next_g or {}).get('meters')
            status = 'over' if status == 'over' or not nxt or t not in nxt else 'warn'
        rep.add('time signature', status, ', '.join(dict.fromkeys(t for _, t in times)) +
                ('' if status == 'ok' else f'; this level uses {", ".join(g["meters"])}'))
    if len({t[1] for t in times}) > 1:
        rep.add('time changes', 'warn', 'meter changes at bars ' + ', '.join(str(t[0]) for t in times[1:]))
    # Length
    if g.get('bars'):
        lo, hi = g['bars']
        rep.add('length', 'ok' if lo <= bars <= hi else 'warn', f'{bars} bars (this level is usually {lo}–{hi})')
    # Rhythm
    ok_share = g.get('sixteenth_share_ok')
    if ok_share is not None:
        if ok_share == 0:
            short = [n for n in notes if n.type in SHORT_TYPES or (n.type == 'eighth' and n.dots)]
            rep.add('shortest notes', 'over' if short else 'ok',
                    f'{len(short)} notes shorter than an eighth (or dotted eighths), bars {bars_of(short)}' if short
                    else 'eighths or longer', short)
        else:
            short = [n for n in notes if n.type in SHORT_TYPES]
            share = len(short) / max(1, len(notes))
            status = band(share, ok_share, ok_share + 0.25)
            rep.add('shortest notes', status, f'{share:.0%} of notes are sixteenths or shorter (this level up to {ok_share:.0%})',
                    short if status != 'ok' else ())
    tiny = [n for n in notes if n.type in TINY_TYPES]
    if tiny and g.get('thirty_seconds'):
        rep.add('32nd notes', g['thirty_seconds'], f'{len(tiny)} notes of 32nd or shorter, bars {bars_of(tiny)}',
                tiny if g['thirty_seconds'] != 'ok' else ())
    tup = [n for n in notes if n.tuplet]
    if tup and g.get('triplets', 'ok') != 'ok':
        rep.add('tuplets', g['triplets'], f'{len(tup)} tuplet notes, bars {bars_of(tup)}', tup)
    grace = [n for n in notes if n.grace]
    if grace and g.get('grace', 'ok') != 'ok':
        rep.add('grace notes', g['grace'], f'{len(grace)} grace notes, bars {bars_of(grace)}', grace)
    # Accidentals outside the key
    per_bar = g.get('accidentals_per_bar')
    if per_bar is not None and pitched:
        scale = key_scale((info['keys'] or [(1, 0, 'major')])[0][1])
        acc = [n for n in pitched if (n.midi % 12) not in scale]
        limit = max(2, per_bar * bars)
        rep.add('accidentals', 'ok' if len(acc) <= limit else 'warn',
                f'{len(acc)} notes outside the key signature (this level about {per_bar:g} a bar)',
                acc if len(acc) > limit else ())
    # Notation features
    for field, key, label in (('pedal', 'pedal', 'pedal'), ('ottava', 'octave_shift', 'octave lines'),
                              ('clef_change', 'clef_changes', 'clef changes')):
        status = g.get(field)
        if status and status != 'ok' and info[key]:
            where = ', '.join(map(str, sorted(set(info[key]))))
            rep.add(label, status, f'{label} at bars {where}; not expected at this level')
    # Tempo and density
    tempo, assumed = tempo_of(info)
    if g.get('tempo_max') and info['tempo']:
        fast = max(t for _, t in info['tempo'])
        rep.add('tempo', 'ok' if fast <= g['tempo_max'] else 'warn',
                f'up to {fast:g} quarter notes a minute (this level up to {g["tempo_max"]})')


def density(notes, info, profile, key):
    """Notes per second against recordings labelled with this grade (PSyllabus), piano only."""
    dens = profile.get('density')
    if not dens or not info['quarters']:
        return None
    counted = [n for n in notes if not n.grace and not n.tied_from]
    tempo, assumed = tempo_of(info)
    seconds = float(info['quarters']) * 60 / tempo
    rate = len(counted) / seconds
    lo, mid, hi = dens['notes_per_s'][key]
    dur_lo, dur_mid, dur_hi = dens['duration_s'][key]
    tail = f' (tempo {"assumed " if assumed else ""}{tempo:g})'
    status = 'warn' if rate > hi else 'info'
    detail = (f'{rate:.1f} notes a second{tail}; recordings at this grade: median {mid}, 90% under {hi}. '
              f'Length about {seconds:.0f} s without repeats; typical {dur_lo:.0f}–{dur_hi:.0f} s, median {dur_mid:.0f}')
    return status, detail


def check_keyboard(notes, info, g, rep):
    bars = info['bars']
    for hand in ('RH', 'LH'):
        hn = [n for n in notes if n.hand == hand and not n.grace and n.midi is not None]
        if not hn:
            rep.add(f'{hand} present', 'warn', f'no {hand} notes')
            continue
        by_onset = defaultdict(list)
        for n in hn:
            by_onset[n.onset].append(n)
        onsets = sorted(by_onset)
        stacks = [by_onset[o] for o in onsets]
        struck = [[n for n in s if not n.tied_from] for s in stacks]
        # Notes at once
        over_at, warn_at = g.get('chord_over_at'), g.get('chord_warn_at')
        if over_at:
            big = [s for s in struck if len(s) >= over_at]
            if big:
                rep.add(f'{hand} notes at once', 'over', f'{len(big)} chords of {over_at}+ notes, bars {bars_of([s[0] for s in big])}',
                        [n for s in big for n in s])
        if warn_at and not (over_at and any(len(s) >= over_at for s in struck)):
            many = [s for s in struck if len(s) >= warn_at]
            share = len(many) / max(1, len(stacks))
            limit = g.get('chord_warn_share', 1.0)
            rep.add(f'{hand} notes at once', 'ok' if share <= limit else 'warn',
                    f'at most {max([len(s) for s in struck] or [1])}; {warn_at}+ notes together on {share:.0%} of onsets'
                    + ('' if share <= limit else ' (keep them occasional)'),
                    [n for s in many for n in s] if share > limit else ())
        # Stretch of notes struck together
        if g.get('stretch'):
            sw, so = g['stretch']
            wide = [s for s in struck if len(s) >= 2 and max(n.midi for n in s) - min(n.midi for n in s) > sw]
            if wide:
                over = [s for s in wide if max(n.midi for n in s) - min(n.midi for n in s) > so]
                rep.add(f'{hand} stretch', 'over' if over else 'warn',
                        f'{len(wide)} chords or intervals wider than {sw} semitones, bars {bars_of([s[0] for s in wide])}',
                        [n for s in wide for n in s])
        if g.get('voices_warn'):
            voices = {n.voice for n in hn}
            if len(voices) > 1:
                rep.add(f'{hand} voices', 'warn', f'{len(voices)} voices in one hand; this level has one line per hand')
        # Range and leaps (top line for RH, bottom line for LH)
        line = [max(s, key=lambda n: n.midi) if hand == 'RH' else min(s, key=lambda n: n.midi) for s in stacks]
        lo, hi = min(n.midi for n in hn), max(n.midi for n in hn)
        if g.get('hand_span'):
            ws, wo = g['hand_span']
            rep.add(f'{hand} range', band(hi - lo, ws, wo), f'{name_of(lo)}–{name_of(hi)} ({hi - lo} semitones; comfortable up to {ws})')
        if g.get('leap'):
            lw, lo_over = g['leap']
            # A jump after a rest or a long note (half or longer) gives the hand time to move,
            # so only count jumps between connected notes.
            joined = [(a, b) for a, b in zip(line, line[1:]) if a.dur < 2 and b.time <= a.time + a.dur]
            leaps = [b for a, b in joined if abs(b.midi - a.midi) > lo_over]
            mid = [b for a, b in joined if lw < abs(b.midi - a.midi) <= lo_over]
            if leaps:
                rep.add(f'{hand} leaps', 'over', f'{len(leaps)} jumps over {lo_over} semitones between connected notes, bars {bars_of(leaps)}', leaps)
            elif len(mid) > max(2, bars // 8):
                rep.add(f'{hand} leaps', 'warn', f'{len(mid)} jumps over {lw} semitones, bars {bars_of(mid)}', mid)
        if g.get('ledger'):
            low_lim, high_lim = (g['ledger'][0], g['ledger'][1]) if hand == 'RH' else (g['ledger'][2], g['ledger'][3])
            ledger = [n for n in hn if n.midi < low_lim or n.midi > high_lim]
            if len(ledger) > max(2, len(hn) // 20):
                rep.add(f'{hand} ledger lines', 'warn', f'{len(ledger)} notes beyond one ledger line, bars {bars_of(ledger)}', ledger)
        if g.get('positions8') and g.get('position_window'):
            shifts, _ = window_shifts(line, g['position_window'])
            per8 = shifts / max(1, bars) * 8
            ws, wo = g['positions8']
            rep.add(f'{hand} hand positions', band(per8, ws, wo), f'{shifts} moves out of a {g["position_window"]}-semitone position ({per8:.1f} per 8 bars)')
        if hand == 'LH' and g.get('lh_pace'):
            quick = [s[0] for s in stacks if s[0].dur < 1]
            share_q = len(quick) / len(stacks)
            ws, wo = g['lh_pace']
            rep.add('LH pace', band(share_q, ws, wo), f'{share_q:.0%} of LH onsets are eighths or shorter (this level up to {ws:.0%})',
                    quick if share_q > ws else ())
    if g.get('both_eighths_per_bar'):
        rh_q = {n.onset for n in notes if n.hand == 'RH' and n.dur < 1}
        lh_q = {n.onset for n in notes if n.hand == 'LH' and n.dur < 1}
        both = rh_q & lh_q
        if len(both) > max(4, bars * g['both_eighths_per_bar']):
            rep.add('hands together in eighths', 'warn', f'{len(both)} eighth-note onsets in both hands at once')


def check_line(notes, info, g, rep, profile):
    """One melodic part: strings, winds, voice, guitar melody."""
    pitched = [n for n in notes if n.midi is not None and not n.grace]
    if not pitched:
        rep.add('notes', 'warn', 'no pitched notes in this part')
        return
    bars = info['bars']
    by_onset = defaultdict(list)
    for n in pitched:
        by_onset[n.onset].append(n)
    stacks = [by_onset[o] for o in sorted(by_onset)]
    struck = [[n for n in s if not n.tied_from] for s in stacks]
    over_at, warn_at = g.get('chord_over_at'), g.get('chord_warn_at')
    if over_at:
        big = [s for s in struck if len(s) >= over_at]
        if big:
            rep.add('notes at once', 'over', f'{len(big)} places with {over_at}+ notes together, bars {bars_of([s[0] for s in big])}',
                    [n for s in big for n in s])
    if warn_at and not (over_at and any(len(s) >= over_at for s in struck)):
        many = [s for s in struck if len(s) >= warn_at]
        share = len(many) / max(1, len(stacks))
        limit = g.get('chord_warn_share', 0)
        if many:
            rep.add('notes at once', 'ok' if share <= limit else 'warn',
                    f'{warn_at}+ notes together on {share:.0%} of onsets (this level up to {limit:.0%})',
                    [n for s in many for n in s] if share > limit else ())
    if g.get('range'):
        lo_lim, hi_lim = g['range']
        slack = g.get('range_slack', 3)
        out = [n for n in pitched if n.midi < lo_lim or n.midi > hi_lim]
        far = [n for n in out if n.midi < lo_lim - slack or n.midi > hi_lim + slack]
        lo, hi = min(n.midi for n in pitched), max(n.midi for n in pitched)
        status = 'over' if far else ('warn' if out else 'ok')
        rep.add('range', status,
                f'{name_of(lo)}–{name_of(hi)}; this level {name_of(lo_lim)}–{name_of(hi_lim)} (written pitch)' +
                (f'; {len(out)} notes outside, bars {bars_of(out)}' if out else ''), out if out else ())
    if g.get('span'):
        sw, so = g['span']
        lo, hi = min(n.midi for n in pitched), max(n.midi for n in pitched)
        rep.add('span', band(hi - lo, sw, so), f'{name_of(lo)}–{name_of(hi)} ({hi - lo} semitones; this level up to {sw}, a little more is tolerable)')
    if g.get('leap'):
        lw, lo_over = g['leap']
        line = [max(s, key=lambda n: n.midi) for s in stacks]
        joined = [(a, b) for a, b in zip(line, line[1:]) if b.time <= a.time + a.dur]
        leaps = [b for a, b in joined if abs(b.midi - a.midi) > lo_over]
        mid = [b for a, b in joined if lw < abs(b.midi - a.midi) <= lo_over]
        if leaps:
            rep.add('leaps', 'over', f'{len(leaps)} jumps over {lo_over} semitones between connected notes, bars {bars_of(leaps)}', leaps)
        elif len(mid) > max(2, bars // 8):
            rep.add('leaps', 'warn', f'{len(mid)} jumps over {lw} semitones, bars {bars_of(mid)}', mid)
    if g.get('breath_s'):
        tempo, assumed = tempo_of(info)
        ws, wo = g['breath_s']
        runs = runs_of(pitched, Fraction(g.get('breath_gap', 0.5)).limit_denominator(8))
        longest = max(runs, key=lambda r: r[-1].time + r[-1].dur - r[0].time)
        seconds = float(longest[-1].time + longest[-1].dur - longest[0].time) * 60 / tempo
        rep.add('breathing', band(seconds, ws, wo),
                f'longest unbroken phrase about {seconds:.0f} s from bar {longest[0].bar}{" (tempo assumed)" if assumed else ""}; '
                f'this level up to {ws} s (our estimate, not from the syllabus)',
                longest if seconds > ws else ())


def check_percussion(notes, info, g, rep):
    hits = [n for n in notes if not n.grace]
    if not hits:
        rep.add('notes', 'warn', 'no percussion notes in this part')
        return
    by_onset = defaultdict(list)
    for n in hits:
        by_onset[n.onset].append(n)
    stacks = list(by_onset.values())
    if g.get('chord_over_at'):
        big = [s for s in stacks if len(s) >= g['chord_over_at']]
        if big:
            rep.add('hits at once', 'over', f'{len(big)} places with {g["chord_over_at"]}+ drums struck together, bars {bars_of([s[0] for s in big])}',
                    [n for s in big for n in s])
    if g.get('chord_warn_at'):
        many = [s for s in stacks if len(s) >= g['chord_warn_at']]
        share = len(many) / len(stacks)
        if many:
            limit = g.get('chord_warn_share', 1.0)
            rep.add('hits at once', 'ok' if share <= limit else 'warn',
                    f'{g["chord_warn_at"]}+ drums together on {share:.0%} of onsets (this level up to {limit:.0%})',
                    [n for s in many for n in s] if share > limit else ())
    if g.get('instruments_max'):
        used = {n.inst for n in hits}
        rep.add('drums used', 'ok' if len(used) <= g['instruments_max'] else 'warn',
                f'{len(used)} different drums or cymbals (this level up to {g["instruments_max"]})')
    if g.get('hits_per_bar'):
        per_bar = len(hits) / max(1, info['bars'])
        ws, wo = g['hits_per_bar']
        rep.add('density', band(per_bar, ws, wo), f'{per_bar:.1f} hits a bar (this level up to {ws})')


def run_checks(notes, info, profile, key, next_key, ignore=()):
    g = profile['grades'][key]
    next_g = profile['grades'].get(next_key) if next_key else None
    rep = Report(ignore)
    kind = profile['kind']
    check_common(notes, info, g, next_g, rep, kind)
    if kind == 'keyboard':
        check_keyboard(notes, info, g, rep)
    elif kind == 'percussion':
        check_percussion(notes, info, g, rep)
    else:
        check_line(notes, info, g, rep, profile)
    if kind == 'keyboard' and profile.get('density'):
        found = density(notes, info, profile, key)
        if found:
            rep.add('density', *found)
    return rep


def verdict(profile, key, results):
    label = grade_label(profile, key)
    statuses = [r['status'] for r in results]
    if 'over' in statuses:
        return f'above {label}'
    warns = statuses.count('warn')
    if warns > 2:
        return f'close to {label}, with several harder spots'
    return f'about {label}' if not warns else f'about {label}, with a few harder spots'


def grade_order(profile):
    return sorted(profile['grades'], key=lambda k: (not k.lstrip('-').isdigit(), int(k) if k.lstrip('-').isdigit() else 0, k))


def estimate(notes, info, profile, ignore=()):
    order = grade_order(profile)
    rows, lowest, likely = [], None, None
    for i, key in enumerate(order):
        rep = run_checks(notes, info, profile, key, order[i + 1] if i + 1 < len(order) else None, ignore)
        over = [r['check'] for r in rep.results if r['status'] == 'over']
        warn = [r['check'] for r in rep.results if r['status'] == 'warn']
        rows.append({'grade': key, 'label': grade_label(profile, key), 'over': over, 'warn': warn})
        if lowest is None and not over:
            lowest = key
        if likely is None and not over and len(warn) <= 2:
            likely = key
    return rows, lowest, likely


def list_profiles():
    for path in profile_files():
        p = json.loads(path.read_text(encoding='utf-8'))
        print(f"{p['instrument']:<17} grades {', '.join(grade_order(p)):<26} confidence {p.get('confidence', '?'):<7} {p['system']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('score', nargs='?')
    parser.add_argument('--instrument', default='piano', help='profile name (see --list)')
    parser.add_argument('--grade', default='1', help='grade key in the profile, e.g. 1')
    parser.add_argument('--part', type=int, default=1, help='part number to check for single-line instruments')
    parser.add_argument('--written-offset', type=int, help='semitones from concert to written pitch (overrides the profile; saxophone: soprano 2, alto 9, tenor 14, baritone 21)')
    parser.add_argument('--as-written', action='store_true', help='pitches are already written pitch (skip the concert-to-written shift)')
    parser.add_argument('--estimate', action='store_true', help='report the lowest grade with no check over')
    parser.add_argument('--json', action='store_true', help='print JSON instead of text')
    parser.add_argument('--mark', help='write a copy with notes that broke a check coloured red')
    parser.add_argument('--ignore', default='', help='comma-separated check names to report as info only, e.g. range,key (for an instrument that borrows another instrument\'s profile)')
    parser.add_argument('--list', action='store_true', help='list available profiles')
    args = parser.parse_args()
    if args.list:
        list_profiles()
        return
    if not args.score:
        parser.error('score file required')
    ignore = [x.strip() for x in args.ignore.split(',') if x.strip()]
    profile = load_profile(args.instrument)
    tree = load(args.score)
    notes, info = read_score(tree, profile['kind'], args.part)
    if not notes:
        sys.exit('No notes found: is this a MusicXML score?')
    shift_note = None
    offset = args.written_offset if args.written_offset is not None else profile.get('written_offset', 0)
    if offset and not info['has_transpose'] and not args.as_written:
        to_written(notes, info, offset)
        shift_note = (f'No transposition in the file, so the pitches are read as concert pitch and moved up {offset} semitones '
                      f'to the written pitch this profile uses (--as-written turns this off)')
    if args.estimate:
        rows, lowest, likely = estimate(notes, info, profile, ignore)
        reliable = profile.get('reliable_up_to')
        out = {'instrument': profile['instrument'], 'lowest_grade_with_nothing_over': lowest, 'likely_grade': likely, 'grades': rows,
               'confidence': profile.get('confidence'), 'reliable_up_to': reliable}
        if args.json:
            print(json.dumps(out, ensure_ascii=False, indent=2))
            return
        print(f"{profile['instrument']} ({profile['system']}), confidence {profile.get('confidence', '?')}")
        if shift_note:
            print(f'({shift_note})')
        for r in rows:
            print(f"{r['label']:>10}: over {len(r['over'])}" + (f" ({', '.join(r['over'])})" if r['over'] else '') +
                  f", warn {len(r['warn'])}")
        print('\nLowest level with nothing over: ' + (grade_label(profile, lowest) if lowest else 'none, above the top of this profile'))
        print('Likely level (nothing over, at most two warnings): ' + (grade_label(profile, likely) if likely else 'none'))
        top = likely or lowest
        if reliable is not None and top is not None and int(top) > reliable:
            print(f'Note: above grade {reliable} this profile mostly leaves limits open, so read the result as "at least".')
        return
    key = grade_key(profile, args.grade)
    order = grade_order(profile)
    nxt = order[order.index(key) + 1] if order.index(key) + 1 < len(order) else None
    rep = run_checks(notes, info, profile, key, nxt, ignore)
    summary = {'instrument': profile['instrument'], 'system': profile['system'], 'grade': key,
               'confidence': profile.get('confidence'), 'verdict': verdict(profile, key, rep.results),
               'bars': info['bars'], 'checks': rep.results}
    if args.mark:
        for n in notes:
            if id(n.el) in rep.flagged:
                n.el.set('color', RED)
                for child in ('notehead', 'stem', 'beam', 'accidental'):
                    for c in n.el.findall(child):
                        c.set('color', RED)
        tree.write(args.mark, encoding='utf-8', xml_declaration=True)
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return
    print(f"Profile: {profile['instrument']} ({profile['system']}), {grade_label(profile, key)}, confidence {profile.get('confidence', '?')}")
    if shift_note:
        print(f'({shift_note})')
    if profile['kind'] != 'keyboard' and info['parts'] > 1:
        print(f'(checked part {args.part} of {info["parts"]}; use --part to pick another)')
    for r in rep.results:
        print(f"{r['status']:>4}  {r['check']}: {r['detail']}")
    print(f"\nVerdict: {summary['verdict']}")


if __name__ == '__main__':
    main()
