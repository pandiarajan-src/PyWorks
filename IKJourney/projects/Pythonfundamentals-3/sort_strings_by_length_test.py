import unittest
from sort_strings_by_length import sort_string_by_len_brute_force, \
    sort_string_by_len_using_map


class TestSortStringsByLength(unittest.TestCase):
    def test_sort_string_by_len_brute_force(self):
        self.assertListEqual(
            sort_string_by_len_brute_force(["sam", "Johnathan", "Jamie", "Jeff", "Jeff", "sa", "Marina"]),
            ["sa", "sam", "Jeff", "Jeff", "Jamie", "Marina", "Johnathan"])
        self.assertListEqual(
            sort_string_by_len_brute_force(["there", "hi", "test", "hello", "how", "are"]),
            ["hi", "are", "how", "test", "hello", "there"])

    def test_sort_string_by_len_using_map(self):
        self.assertListEqual(
            sort_string_by_len_using_map(["sam", "Johnathan", "Jamie", "Jeff", "Jeff", "sa", "Marina"]),
            ["sa", "sam", "Jeff", "Jeff", "Jamie", "Marina", "Johnathan"])
        self.assertListEqual(
            sort_string_by_len_using_map(["there", "hi", "test", "hello", "how", "are"]),
            ["hi", "how", "are", "test", "there", "hello"])


if __name__ == '__main__':
    unittest.main()
