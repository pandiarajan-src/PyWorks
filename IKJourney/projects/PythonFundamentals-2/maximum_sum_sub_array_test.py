import unittest
from maximum_sum_sub_array import maximum_sub_array_kadane_algorithm, \
    maximum_sub_array_neet_code_sample, maximum_sub_array_brute_force_dual_loop, \
    maximum_sub_array_brute_force_three_loop


class TestMaximumSumSubArray(unittest.TestCase):
    def test_maximum_sub_array_kadane_algorithm(self):
        self.assertEqual(maximum_sub_array_kadane_algorithm([2, -6, 3, 4, -5]), 7)
        self.assertEqual(maximum_sub_array_kadane_algorithm([-7, -9, -3, -5]), -3)
        self.assertEqual(maximum_sub_array_kadane_algorithm([-10000]), -10000)
        self.assertEqual(maximum_sub_array_kadane_algorithm([-10, 10000]), 10000)
        self.assertEqual(maximum_sub_array_kadane_algorithm([0, 10000]), 10000)
        self.assertEqual(maximum_sub_array_kadane_algorithm([10, 10000]), 10010)
        self.assertEqual(maximum_sub_array_kadane_algorithm([0, 0, 0, -1, 0]), 0)
        self.assertEqual(maximum_sub_array_kadane_algorithm([-1, -1, -1, 0, -1]), 0)
        self.assertEqual(maximum_sub_array_kadane_algorithm([-1, 2, -5, 3, 0]), 3)
        self.assertEqual(maximum_sub_array_kadane_algorithm([-10, -12, -39, -11, -10]), -10)
        self.assertEqual(maximum_sub_array_kadane_algorithm([1, 6, 7, -8, -2, 6, 10]), 20)
        self.assertEqual(maximum_sub_array_kadane_algorithm([-8, -10, -3, 9, -2, -98, -41]), 9)
        self.assertEqual(maximum_sub_array_kadane_algorithm([2, 1, -4, 3, -2, 5, -6, 2, 3]), 6)

    def test_maximum_sub_array_neet_code_sample(self):
        self.assertEqual(maximum_sub_array_neet_code_sample([2, -6, 3, 4, -5]), 7)
        self.assertEqual(maximum_sub_array_neet_code_sample([-7, -9, -3, -5]), -3)
        self.assertEqual(maximum_sub_array_neet_code_sample([-10000]), -10000)
        self.assertEqual(maximum_sub_array_neet_code_sample([-10, 10000]), 10000)
        self.assertEqual(maximum_sub_array_neet_code_sample([0, 10000]), 10000)
        self.assertEqual(maximum_sub_array_neet_code_sample([10, 10000]), 10010)
        self.assertEqual(maximum_sub_array_neet_code_sample([0, 0, 0, -1, 0]), 0)
        self.assertEqual(maximum_sub_array_neet_code_sample([-1, -1, -1, 0, -1]), 0)
        self.assertEqual(maximum_sub_array_neet_code_sample([-1, 2, -5, 3, 0]), 3)
        self.assertEqual(maximum_sub_array_neet_code_sample([-10, -12, -39, -11, -10]), -10)
        self.assertEqual(maximum_sub_array_neet_code_sample([1, 6, 7, -8, -2, 6, 10]), 20)
        self.assertEqual(maximum_sub_array_neet_code_sample([-8, -10, -3, 9, -2, -98, -41]), 9)
        self.assertEqual(maximum_sub_array_neet_code_sample([2, 1, -4, 3, -2, 5, -6, 2, 3]), 6)

    def test_maximum_sub_array_brute_force_dual_loop(self):
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([2, -6, 3, 4, -5]), 7)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([-7, -9, -3, -5]), -3)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([-10000]), -10000)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([-10, 10000]), 10000)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([0, 10000]), 10000)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([10, 10000]), 10010)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([0, 0, 0, -1, 0]), 0)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([-1, -1, -1, 0, -1]), 0)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([-1, 2, -5, 3, 0]), 3)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([-10, -12, -39, -11, -10]), -10)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([1, 6, 7, -8, -2, 6, 10]), 20)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([-8, -10, -3, 9, -2, -98, -41]), 9)
        self.assertEqual(maximum_sub_array_brute_force_dual_loop([2, 1, -4, 3, -2, 5, -6, 2, 3]), 6)

    def test_maximum_sub_array_brute_force_three_loop(self):
        self.assertEqual(maximum_sub_array_brute_force_three_loop([2, -6, 3, 4, -5]), 7)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([-7, -9, -3, -5]), -3)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([-10000]), -10000)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([-10, 10000]), 10000)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([0, 10000]), 10000)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([10, 10000]), 10010)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([0, 0, 0, -1, 0]), 0)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([-1, -1, -1, 0, -1]), 0)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([-1, 2, -5, 3, 0]), 3)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([-10, -12, -39, -11, -10]), -10)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([1, 6, 7, -8, -2, 6, 10]), 20)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([-8, -10, -3, 9, -2, -98, -41]), 9)
        self.assertEqual(maximum_sub_array_brute_force_three_loop([2, 1, -4, 3, -2, 5, -6, 2, 3]), 6)


if __name__ == '__main__':
    unittest.main()
