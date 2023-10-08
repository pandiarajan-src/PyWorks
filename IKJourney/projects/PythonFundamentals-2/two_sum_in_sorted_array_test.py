import unittest
from two_sum_in_sorted_array import pair_sum_sorted_array_normal_case, pair_sum_sorted_array_two_pointers


class TestTwoSumInASortedArray(unittest.TestCase):

    def test_two_sum_in_a_sorted_array_normal_case(self):
        self.assertListEqual(pair_sum_sorted_array_normal_case([1, 2, 3, 5, 10], 7), [1, 3])

    def test_two_sum_in_a_sorted_array_two_pointer(self):
        self.assertListEqual(pair_sum_sorted_array_two_pointers([1, 2, 3, 5, 10], 7), [1, 3])
        self.assertListEqual(pair_sum_sorted_array_two_pointers([-10, -7, -5, 0, 8, 10], 3), [1, 5])
        self.assertListEqual(pair_sum_sorted_array_two_pointers([1, 2], 7), [-1, -1])
        self.assertListEqual(pair_sum_sorted_array_two_pointers([1, 2], 7), [-1, -1])


if __name__ == "__main__":
    unittest.main()
