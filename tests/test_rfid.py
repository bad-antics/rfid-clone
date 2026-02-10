import unittest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from rfid_clone.core import MifareClassic, EM410x

class TestMifare(unittest.TestCase):
    def test_parse_invalid(self):
        m = MifareClassic()
        with self.assertRaises(ValueError):
            m.parse_dump(b"too short")
    def test_init(self):
        m = MifareClassic()
        self.assertEqual(m.SECTORS_1K, 16)

class TestEM410x(unittest.TestCase):
    def test_short_bits(self):
        e = EM410x()
        self.assertIsNone(e.decode_id([0]*10))

if __name__ == "__main__": unittest.main()
