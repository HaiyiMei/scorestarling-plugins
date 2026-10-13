"""Read-only artifact comparisons distinguish byte identity, PDF content and incomplete checks."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/scorestarling-score/scripts/compare_artifacts.py'
spec = importlib.util.spec_from_file_location('compare_artifacts', SCRIPT)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
try:
    import fitz
except ImportError:
    fitz = None


class Comparison(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_bytes_and_prefix_are_distinct(self):
        a, b = self.root / 'before.bin', self.root / 'after.bin'
        a.write_bytes(b'original\0\xff')
        b.write_bytes(a.read_bytes())
        self.assertTrue(helper.compare(a, b)['byte_identical'])
        b.write_bytes(a.read_bytes() + b' appended provenance')
        result = helper.compare(a, b)
        self.assertTrue(result['before_is_prefix_of_after'])
        self.assertFalse(result['same_content'])
        self.assertFalse(result['signature_trust_verified'])
        self.assertFalse(helper.compare(b, a)['before_is_prefix_of_after'])
        failed = subprocess.run([sys.executable, str(SCRIPT), str(a), str(b), '--require-same-content'], capture_output=True)
        self.assertEqual(failed.returncode, 1)
        self.assertEqual(a.read_bytes(), b'original\0\xff')

    def test_missing_input_is_not_a_completed_comparison(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '/not-a-file', '/not-a-file'], capture_output=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn(b'"comparison_completed": false', result.stderr)

    @unittest.skipUnless(fitz, 'PyMuPDF unavailable: byte checks run, PDF checks are not verified')
    def test_pdf_metadata_change_and_content_change(self):
        a, b, c = [self.root / name for name in ['before.pdf', 'metadata.pdf', 'changed.pdf']]
        with fitz.open() as doc:
            doc.new_page().insert_text((40, 60), 'C natural')
            doc.save(a)
        with fitz.open(a) as doc:
            doc.set_metadata({'title': 'delivery metadata'})
            doc.save(b)
        result = helper.compare(a, b, pdf=True)
        self.assertFalse(result['byte_identical'])
        self.assertTrue(result['same_content'])
        self.assertEqual(len(result['pdf']['pages']), 1)
        with fitz.open() as doc:
            doc.new_page().insert_text((40, 60), 'D flat')
            doc.save(c)
        result = helper.compare(a, c, pdf=True)
        self.assertFalse(result['same_content'])
        self.assertFalse(result['pdf']['pages'][0]['raster_equal'])
        with fitz.open(b) as doc:
            doc.new_page()
            extra = self.root / 'extra.pdf'
            doc.save(extra)
        self.assertFalse(helper.compare(a, extra, pdf=True)['same_content'])


if __name__ == '__main__':
    unittest.main()
