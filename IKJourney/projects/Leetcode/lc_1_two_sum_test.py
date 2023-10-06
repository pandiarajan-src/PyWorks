import unittest
import timeit
from lc_1_two_sum import TwoSumSolution


class TestTwoSumSolution(unittest.TestCase):

    def test_naive_two_sum_solution(self):
        self.assertListEqual([0, 1], TwoSumSolution.naive_two_sum([2, 7, 11, 15], 9))
        self.assertListEqual([1, 2], TwoSumSolution.naive_two_sum([3, 2, 4], 6))
        self.assertListEqual([0, 1], TwoSumSolution.naive_two_sum([3, 3], 6))
        self.assertListEqual([], TwoSumSolution.naive_two_sum([], 6))
        self.assertListEqual([], TwoSumSolution.naive_two_sum([1, 2, 3, 4, 5], 25))

    def test_optimized_two_sum_solution(self):
        self.assertListEqual([0, 1], TwoSumSolution.optimized_two_sum([2, 7, 11, 15], 9))
        self.assertListEqual([1, 2], TwoSumSolution.optimized_two_sum([3, 2, 4], 6))
        self.assertListEqual([1, 0], TwoSumSolution.optimized_two_sum([3, 3], 6))
        self.assertListEqual([], TwoSumSolution.optimized_two_sum([], 6))
        self.assertListEqual([], TwoSumSolution.optimized_two_sum([1, 2, 3, 4, 5], 25))


if __name__ == "__main__":
    unittest.main()

