import unittest
from reverse_words_in_string import reverse_words_in_string


class TestReverseWordInString(unittest.TestCase):

    def test_reverse_words_in_string(self):
        self.assertEqual("courses prep interview technical best",
                         reverse_words_in_string("best technical interview prep courses"))
        self.assertEqual("kickstart",
                         reverse_words_in_string("kickstart"))
        self.assertEqual("b", reverse_words_in_string("b"))
        self.assertEqual('aaaaaaaaaaaaa', reverse_words_in_string("aaaaaaaaaaaaa"))
        self.assertEqual("a a a a a a a a a a a", reverse_words_in_string("a a a a a a a a a a a"))


if __name__ == '__main__':
    unittest.main()
