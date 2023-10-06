import unittest
from pivot_index import get_pivot_index


class TestPivotIndex(unittest.TestCase):

    def test_find_pivot_index_success(self):
        self.assertEqual(2, get_pivot_index([2, 3, 1, -1, 1, 1, 4]))
        self.assertEqual(-1, get_pivot_index([2, 3, 5]))
        self.assertEqual(0, get_pivot_index([0, 1, -1]))
        self.assertEqual(6, get_pivot_index([1, 2, 3, 4, 5, -15, 7]))
        self.assertEqual(0, get_pivot_index([10000]))
        self.assertEqual(0, get_pivot_index([0, 0, 0, 0, 0, 0, 0, 0]))
        self.assertEqual(12, get_pivot_index([1, 2, -3, 1, 2, 3, -6, 1, 2, 3, 4, -10, 0, -100000, 100000]))
        self.assertEqual(-1, get_pivot_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertEqual(12, get_pivot_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -55, 0, 0]))


if __name__ == '__main__':
    unittest.main()
