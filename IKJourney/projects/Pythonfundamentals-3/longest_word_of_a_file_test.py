import unittest
from longest_word_of_a_file import find_longest_word_in_a_file


class TestLongestWordOfAFile(unittest.TestCase):
    def test_find_longest_word_in_a_file(self):
        self.assertEqual(find_longest_word_in_a_file('english_words.txt'), "longest")


if __name__ == '__main__':
    unittest.main()
