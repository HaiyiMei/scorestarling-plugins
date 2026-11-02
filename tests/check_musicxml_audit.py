"""Synthetic notation audits catch write regressions without judging the recording or rewriting files."""
# size: medium

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/scorestarling-score/scripts/audit_musicxml.py'
spec = importlib.util.spec_from_file_location('audit_musicxml', SCRIPT)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def score(notes, divisions=8):
    return f'<score-partwise><part id="P1"><measure number="1"><attributes><divisions>{divisions}</divisions></attributes>{notes}</measure></part></score-partwise>'


def note(ident, pitch='C', duration=2, extra=''):
    return f'<note id="{ident}">{extra}<pitch><step>{pitch}</step><octave>4</octave></pitch><duration>{duration}</duration><voice>1</voice><type>16th</type><staff>1</staff></note>'


class Audit(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)

    def write(self, name, body):
        path = self.folder / name
        path.write_text(body)
        return path

    def test_beaming_is_a_scoped_advisory_not_a_musical_verdict(self):
        body = score(''.join(note(f'n{i}') for i in range(4)))
        path = self.write('unbeamed.musicxml', body)
        report, _ = helper.inspect(path)
        self.assertEqual(report['unbeamed_short_runs']['examples'][0]['notes'], 4)
        self.assertEqual(report['unsafe']['count'], 0)
        tree = ET.fromstring(body)
        for i, n in enumerate(tree.findall('.//note')):
            ET.SubElement(n, 'beam', {'number': '1'}).text = 'begin' if i == 0 else 'end' if i == 3 else 'continue'
        beamed = self.write('beamed.musicxml', ET.tostring(tree, encoding='unicode'))
        self.assertEqual(helper.inspect(beamed)[0]['unbeamed_short_runs']['count'], 0)
        result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertFalse(json.loads(result.stdout)['performance_verified'])
        self.assertEqual(path.read_text(), body)

    def test_octave_and_clef_changes_cannot_split_a_chord(self):
        for direction in (
            '<direction><direction-type><octave-shift type="down" size="8"/></direction-type></direction>',
            '<attributes><clef><sign>G</sign><line>2</line></clef></attributes>',
        ):
            base, member = note('base'), note('member', 'E', extra='<chord/>')
            bad = self.write('bad.musicxml', score(base + direction + member))
            good = self.write('good.musicxml', score(base + member + direction))
            self.assertEqual(helper.inspect(bad)[0]['unsafe']['examples'][0]['kind'], 'direction_inside_chord')
            self.assertEqual(helper.inspect(good)[0]['unsafe']['count'], 0)

    def test_tie_heads_are_not_removed_attacks_and_resolution_is_inherited(self):
        body = score(
            note('held', duration=2) + note('tail', duration=2, extra='<tie type="stop"/>') + note('next', 'D')
        )
        before = self.write('before.musicxml', body)
        after = self.write('after.musicxml', score(note('held', duration=4) + note('next', 'D')))
        a, old = helper.inspect(before)
        b, new = helper.inspect(after)
        self.assertEqual(a['summary']['pitched_attacks'], 2)
        changes = helper.compare(old, new)
        self.assertEqual(changes['removed_attack_ids']['count'], 0)
        self.assertEqual(changes['pitch_changed']['count'], 0)
        self.assertEqual(changes['duration_changed']['examples'], ['held'])
        # The same written quarter at different divisions is not a duration change.
        one = helper.inspect(self.write('div4.musicxml', score(note('n', duration=4), divisions=4)))[1]
        two = helper.inspect(self.write('div8.musicxml', score(note('n', duration=8))))[1]
        self.assertEqual(helper.compare(one, two)['duration_changed']['count'], 0)

    def test_grace_conversion_retains_identity_and_repitch_is_reported(self):
        before = helper.inspect(self.write('before.musicxml', score(note('n'))))[1]
        grace = note('n', 'D', extra='<grace slash="yes"/>').replace('<duration>2</duration>', '')
        report, after = helper.inspect(self.write('after.musicxml', score(grace)))
        changes = helper.compare(before, after)
        self.assertEqual(report['summary']['grace_notes'], 1)
        self.assertEqual(changes['removed_attack_ids']['count'], 0)
        self.assertEqual(changes['pitch_changed']['examples'], ['n'])
        self.assertEqual(changes['grace_changed']['examples'], ['n'])

    def test_duplicate_ids_and_unsupported_input_fail_without_writes(self):
        duplicate = self.write('duplicate.musicxml', score(note('n') + note('n')))
        result = subprocess.run([sys.executable, str(SCRIPT), str(duplicate)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)['after']['unsafe']['count'], 1)
        for body in ('<!DOCTYPE score-partwise [<!ENTITY n "expanded">]>' + score(''), '<score-timewise/>'):
            path = self.write('refused.musicxml', body)
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertFalse(json.loads(result.stderr)['audit_completed'])
            self.assertEqual(path.read_text(), body)

    def test_external_musicxml_doctype_needs_no_network(self):
        path = self.write(
            'external-dtd.musicxml',
            '<!DOCTYPE score-partwise SYSTEM "https://example.invalid/musicxml.dtd">' + score(note('n')),
        )
        report, attacks = helper.inspect(path)
        self.assertEqual(report['unsafe']['count'], 0)
        self.assertEqual(set(attacks), {'n'})


if __name__ == '__main__':
    unittest.main()
