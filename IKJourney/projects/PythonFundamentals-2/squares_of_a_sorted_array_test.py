import unittest
from squares_of_a_sorted_array import squares_of_a_sorted_array_naive


class TestSquaresOfASortedArray(unittest.TestCase):
    def test_something(self):
        self.assertListEqual(squares_of_a_sorted_array_naive([1, 2, 3, 4]), [1, 4, 9, 16])
        self.assertListEqual(squares_of_a_sorted_array_naive([-9, -5, -2, 0, 3, 7]), [0, 4, 9, 25, 49, 81])
        self.assertListEqual(squares_of_a_sorted_array_naive([-10, -8, -6, -4, -1]), [1, 16, 36, 64, 100])
        self.assertListEqual(squares_of_a_sorted_array_naive([5]), [25])
        self.assertListEqual(squares_of_a_sorted_array_naive([-557, -557, -557, -557, -557, -557]),
                             [310249, 310249, 310249, 310249, 310249, 310249])
        self.assertListEqual(squares_of_a_sorted_array_naive([-20, -12, -6, -3, 3, 6, 12, 20]),
                             [9, 9, 36, 36, 144, 144, 400, 400])


if __name__ == '__main__':
    unittest.main()
