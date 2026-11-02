"""Read-only notation audit and attack-ID comparison for uncompressed MusicXML; no musical verdict."""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

MAX_BYTES = 16 * 1024 * 1024


def examples(items):
    return {'count': len(items), 'examples': items[:8]}


def read(path):
    with Path(path).open('rb') as source:
        data = source.read(MAX_BYTES + 1)
    if not data or len(data) > MAX_BYTES:
        raise ValueError('Use a non-empty, uncompressed MusicXML file no larger than 16 MiB')
    # External MusicXML DTDs are not fetched; refuse internal entity expansion.
    if b'<!ENTITY' in data.upper():
        raise ValueError('Remove entity declarations before this offline audit')
    root = ET.fromstring(data)
    for element in root.iter():
        element.tag = element.tag.rsplit('}', 1)[-1]
    if root.tag != 'score-partwise':
        raise ValueError('Expected uncompressed score-partwise MusicXML')
    return root


def inspect(path):
    root = read(path)
    counts = Counter()
    unsafe, unbeamed, missing_ids = [], [], []
    attacks, ids = {}, set()
    for part in root.findall('part'):
        divisions = Fraction(1)
        counts['parts'] += 1
        for measure in part.findall('measure'):
            counts['part_measures'] += 1
            location = {'part': part.get('id'), 'measure': measure.get('number')}
            cursor, chord_at, boundary = Fraction(0), None, False
            lanes = defaultdict(list)
            for element in measure:
                if element.tag == 'attributes':
                    divisions = Fraction(element.findtext('divisions', str(divisions)))
                    if divisions <= 0:
                        raise ValueError('MusicXML divisions must be positive')
                    boundary |= element.find('clef') is not None
                elif element.tag == 'direction':
                    boundary |= element.find('direction-type/octave-shift') is not None
                elif element.tag in ('backup', 'forward'):
                    duration = Fraction(element.findtext('duration', '0')) / divisions
                    cursor += duration * (-1 if element.tag == 'backup' else 1)
                    chord_at, boundary = None, False
                elif element.tag == 'note':
                    counts['noteheads'] += 1
                    ident = element.get('id')
                    if ident:
                        if ident in ids:
                            unsafe.append({**location, 'kind': 'duplicate_note_id', 'id': ident})
                        ids.add(ident)
                    grace = element.find('grace') is not None
                    chord = element.find('chord') is not None
                    duration = Fraction(element.findtext('duration', '0')) / divisions
                    if duration < 0 or (not grace and duration == 0):
                        unsafe.append({**location, 'kind': 'invalid_note_duration', 'id': ident})
                    if chord:
                        if chord_at is None:
                            unsafe.append({**location, 'kind': 'chord_without_base', 'id': ident})
                        if boundary:
                            unsafe.append({**location, 'kind': 'direction_inside_chord', 'id': ident})
                        at = chord_at
                    else:
                        at = cursor
                        chord_at, boundary = (at if element.find('rest') is None else None), False
                        if not grace:
                            cursor += duration
                    pitch = element.find('pitch')
                    voice, staff = element.findtext('voice', '1'), element.findtext('staff', '1')
                    if not grace and not chord:
                        lanes[(staff, voice)].append((at, duration, element))
                    counts['rests'] += element.find('rest') is not None
                    counts['rests_shorter_than_eighth'] += element.find('rest') is not None and duration < Fraction(
                        1, 2
                    )
                    counts['grace_notes'] += grace
                    counts['tie_starts'] += element.find('tie[@type="start"]') is not None
                    if pitch is None or element.find('tie[@type="stop"]') is not None:
                        continue
                    counts['pitched_attacks'] += 1
                    if not ident:
                        missing_ids.append(location)
                        continue
                    semitone = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}[pitch.findtext('step')]
                    value = 12 * (int(pitch.findtext('octave')) + 1) + semitone + Fraction(pitch.findtext('alter', '0'))
                    attacks[ident] = {
                        'pitch': value,
                        'position': (part.get('id'), measure.get('number'), at),
                        'duration': duration,
                        'staff': staff,
                        'voice': voice,
                        'grace': grace,
                    }
            for (staff, voice), notes in lanes.items():
                run, end = [], None
                for at, duration, note in [*notes, (None, None, ET.Element('note'))]:
                    short = note.findtext('type') in ('16th', '32nd', '64th') and note.find('rest') is None
                    candidate = short and note.find('beam') is None
                    if run and (not candidate or at != end):
                        if len(run) > 1:
                            unbeamed.append(
                                {**location, 'staff': staff, 'voice': voice, 'notes': len(run), 'ids': run[:8]}
                            )
                        run = []
                    if candidate:
                        run.append(note.get('id'))
                    end = at + duration if at is not None else None
    return {
        'summary': dict(counts),
        'unsafe': examples(unsafe),
        'unbeamed_short_runs': examples(unbeamed),
        'attacks_without_ids': examples(missing_ids),
    }, attacks


def compare(before, after):
    retained = sorted(before.keys() & after.keys())
    result = {
        'retained_attack_ids': len(retained),
        'removed_attack_ids': examples(sorted(before.keys() - after.keys())),
        'added_attack_ids': examples(sorted(after.keys() - before.keys())),
    }
    for field in ('pitch', 'position', 'duration', 'staff', 'voice', 'grace'):
        result[field + '_changed'] = examples(
            [ident for ident in retained if before[ident][field] != after[ident][field]]
        )
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('after', type=Path)
    parser.add_argument('--before', type=Path)
    args = parser.parse_args()
    try:
        report, after = inspect(args.after)
        result = {'after': report, 'performance_verified': False, 'source_accuracy_verified': False}
        if args.before:
            baseline, before = inspect(args.before)
            result.update(before=baseline, changes=compare(before, after))
        print(json.dumps(result, ensure_ascii=False))
        return 1 if report['unsafe']['count'] or (args.before and baseline['unsafe']['count']) else 0
    except (OSError, ET.ParseError, ValueError, KeyError, TypeError, ZeroDivisionError) as error:
        print(json.dumps({'audit_completed': False, 'error': str(error)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
