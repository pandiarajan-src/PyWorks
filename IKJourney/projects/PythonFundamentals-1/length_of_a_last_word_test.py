import unittest
from strings_samples import reverse_words_in_string, find_first_occurrence, \
    count_alphabets, length_of_last_word


class TestStringsSamples(unittest.TestCase):

    def test_reverse_words_in_string(self):
        self.assertEqual("courses prep interview technical best",
                         reverse_words_in_string("best technical interview prep courses"))
        self.assertEqual("kickstart",
                         reverse_words_in_string("kickstart"))
        self.assertEqual("b", reverse_words_in_string("b"))
        self.assertEqual('aaaaaaaaaaaaa', reverse_words_in_string("aaaaaaaaaaaaa"))
        self.assertEqual("a a a a a a a a a a a", reverse_words_in_string("a a a a a a a a a a a"))

    def test_find_first_occurrence_character_string(self):
        self.assertEqual(3, find_first_occurrence("interview", 'e'), "find e in interview should be on 3rd position")
        self.assertEqual(-1, find_first_occurrence("kickstart", 'n'), "find n in kickstart is False, so -1")
        self.assertEqual(-1, find_first_occurrence("", 'm'), "find m in '' is False, so -1")
        self.assertEqual(0, find_first_occurrence("b", 'b'), "find b in 'b' is at 0th position")
        self.assertEqual(0, find_first_occurrence("ppppppp", 'p'), "find p in 'ppppppp' is at 0th position")
        self.assertEqual(10, find_first_occurrence("greatcoders", 's'), "find s in 'greatcoders' is at 10th position")

    def test_count_alphabets(self):
        self.assertEqual(5, count_alphabets("#aBdj12C"))
        self.assertEqual(0, count_alphabets("123 !@#$"))
        self.assertEqual(0, count_alphabets(""))
        self.assertEqual(0, count_alphabets("  "))
        self.assertEqual(1, count_alphabets("A"))
        self.assertEqual(4, count_alphabets("aa AA 11   @# "))
        self.assertEqual(14, count_alphabets("abcedfgIJKLMNO"))

    def test_length_of_a_last_word(self):
        self.assertEqual(5, length_of_last_word(" Hello World  "))
        self.assertEqual(9, length_of_last_word("Interview Kickstart"))
        self.assertEqual(0, length_of_last_word(""))
        self.assertEqual(0, length_of_last_word("   "))
        self.assertEqual(1, length_of_last_word("m"))
        self.assertEqual(1, length_of_last_word("  A  "))
        self.assertEqual(4, length_of_last_word("Frog"))
        self.assertEqual(10, length_of_last_word("I love travelling"))



if __name__ == '__main__':
    unittest.main()
