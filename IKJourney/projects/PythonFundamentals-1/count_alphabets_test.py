import unittest
from count_alphabets import count_alphabets


class TestCountAlphabets(unittest.TestCase):

    def test_count_alphabets(self):
        self.assertEqual(5, count_alphabets("#aBdj12C"))
        self.assertEqual(0, count_alphabets("123 !@#$"))
        self.assertEqual(0, count_alphabets(""))
        self.assertEqual(0, count_alphabets("  "))
        self.assertEqual(1, count_alphabets("A"))
        self.assertEqual(4, count_alphabets("aa AA 11   @# "))
        self.assertEqual(14, count_alphabets("abcedfgIJKLMNO"))


if __name__ == '__main__':
    unittest.main()

