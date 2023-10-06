import unittest
from upper_2_lower import uppercase_2_lowercase


class TestSUpper2Lower(unittest.TestCase):

    def test_uppercase_2_lowercase_conversion(self):
        self.assertEqual("interview", uppercase_2_lowercase("InTerView"))
        self.assertEqual("kickstart", uppercase_2_lowercase("KICKSTART"))
        self.assertEqual("", uppercase_2_lowercase(""))
        self.assertEqual("z", uppercase_2_lowercase("Z"))
        self.assertEqual("aabbccddee", uppercase_2_lowercase("aAbBcCdDeE"))
        self.assertEqual("algorithms", uppercase_2_lowercase("algorithms"))
        self.assertEqual("abcdefghijklmnopqrstuvwxyz", uppercase_2_lowercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))


if __name__ == '__main__':
    unittest.main()
