"""The recording probe refuses long windows and, where librosa is installed, prints a short summary and keeps the
rest in files."""
import importlib.util
import io
import json
import math
import struct
import tempfile
import unittest
import wave
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/scorestarling-score/scripts/probe_passage.py'
spec = importlib.util.spec_from_file_location('probe_passage', SCRIPT)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
try:
    import librosa  # noqa: F401
except ImportError:
    librosa = None


class Probe(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.audio = self.root / 'tone.wav'
        rate = 22050
        with wave.open(str(self.audio), 'wb') as out:
            out.setnchannels(1)
            out.setsampwidth(2)
            out.setframerate(rate)
            frames = bytearray()
            for second, hz in enumerate((440.0, 523.25, 659.25)):
                for i in range(rate):
                    level = 0.5 * math.exp(-3 * i / rate)
                    frames += struct.pack('<h', int(32767 * level * math.sin(2 * math.pi * hz * i / rate)))
            out.writeframes(bytes(frames))

    def test_long_windows_are_refused(self):
        with self.assertRaises(SystemExit):
            helper.probe(self.audio, 0, 40, self.root / 'out')
        with self.assertRaises(SystemExit):
            helper.probe(self.audio, 5, 2, self.root / 'out')

    @unittest.skipIf(librosa is None, 'librosa is not installed')
    def test_summary_is_short_and_data_goes_to_files(self):
        printed = io.StringIO()
        with redirect_stdout(printed):
            helper.probe(self.audio, 0, 3, self.root / 'out')
        lines = printed.getvalue().splitlines()
        self.assertLessEqual(len(lines), helper.MAX_LINES)
        self.assertLess(len(printed.getvalue()), 4000)
        data = json.loads((self.root / 'out/probe.json').read_text())
        self.assertGreaterEqual(len(data['onsets']), 2)
        self.assertIn('cqt_db', data)


if __name__ == '__main__':
    unittest.main()
