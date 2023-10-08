import unittest
from intersection_of_sorted_arrays import intersection_of_two_sorted_array_naive, \
    intersection_of_two_sorted_array


class TestIntersectionOfTwoSortedArrayNaive(unittest.TestCase):
    def test_intersection_of_two_sorted_array_naive(self):
        self.assertEqual(intersection_of_two_sorted_array_naive([1, 2, 2, 6, 7], [2, 2, 7, 7]), [2, 7])
        self.assertEqual(intersection_of_two_sorted_array_naive([1, 4, 10, 12], [5, 9, 11]), [-1])
        self.assertEqual(intersection_of_two_sorted_array_naive([10], [20]), [-1])
        self.assertEqual(intersection_of_two_sorted_array_naive([10], [10]), [10])
        self.assertEqual(intersection_of_two_sorted_array_naive([20, 20], [10, 10, 20]), [20])
        self.assertEqual(intersection_of_two_sorted_array_naive([10, 20], [10, 10, 10]), [10])
        self.assertEqual(intersection_of_two_sorted_array_naive([1, 3, 5, 7, 9], [1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])
        self.assertEqual(intersection_of_two_sorted_array_naive([1, 1, 1, 1, 1], [1, 1, 1]), [1])

    def test_intersection_of_two_sorted_array(self):
        self.assertEqual(intersection_of_two_sorted_array([1, 2, 2, 6, 7], [2, 2, 7, 7]), [2, 7])
        self.assertEqual(intersection_of_two_sorted_array([1, 4, 10, 12], [5, 9, 11]), [-1])
        self.assertEqual(intersection_of_two_sorted_array([10], [20]), [-1])
        self.assertEqual(intersection_of_two_sorted_array([10], [10]), [10])
        self.assertEqual(intersection_of_two_sorted_array([20, 20], [10, 10, 20]), [20])
        self.assertEqual(intersection_of_two_sorted_array([10, 20], [10, 10, 10]), [10])
        self.assertEqual(intersection_of_two_sorted_array([1, 3, 5, 7, 9], [1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])
        self.assertEqual(intersection_of_two_sorted_array([1, 1, 1, 1, 1], [1, 1, 1]), [1])


if __name__ == '__main__':
    unittest.main()
