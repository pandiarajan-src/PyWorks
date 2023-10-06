import unittest
from find_1st_occurence_word import find_first_occurrence


class TestFirstOccurrenceOfWord(unittest.TestCase):

    def test_find_first_occurrence_character_string(self):
        self.assertEqual(3, find_first_occurrence("interview", 'e'), "find e in interview should be on 3rd position")
        self.assertEqual(-1, find_first_occurrence("kickstart", 'n'), "find n in kickstart is False, so -1")
        self.assertEqual(-1, find_first_occurrence("", 'm'), "find m in '' is False, so -1")
        self.assertEqual(0, find_first_occurrence("b", 'b'), "find b in 'b' is at 0th position")
        self.assertEqual(0, find_first_occurrence("ppppppp", 'p'), "find p in 'ppppppp' is at 0th position")
        self.assertEqual(10, find_first_occurrence("greatcoders", 's'), "find s in 'greatcoders' is at 10th position")


if __name__ == '__main__':
    unittest.main()
