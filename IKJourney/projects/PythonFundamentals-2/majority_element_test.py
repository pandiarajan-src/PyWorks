import unittest
from majority_element import find_majority_element_naive, \
    find_majority_element_bayer_moore_method


class TestMajorityOfElement(unittest.TestCase):
    def test_majority_of_element_native(self):
        self.assertEqual(find_majority_element_naive([3, 3, 3, 2, 2, 2, 3]), 3)  # add assertion here
        self.assertEqual(find_majority_element_naive([100000]), 100000)
        self.assertEqual(find_majority_element_naive([-1, -1, -1]), -1)
        self.assertEqual(find_majority_element_naive([0, 0, 1, 1, 0, 0]), 0)
        self.assertEqual(find_majority_element_naive([2, 2, 2, 3, 4]), 2)
        self.assertEqual(find_majority_element_naive([2, 3, 7, 3, 4]), None)

    def test_majority_of_element_moore_logic(self):
        self.assertEqual(find_majority_element_bayer_moore_method([3, 3, 3, 2, 2, 2, 3]), 3)  # add assertion here
        self.assertEqual(find_majority_element_bayer_moore_method([100000]), 100000)
        self.assertEqual(find_majority_element_bayer_moore_method([-1, -1, -1]), -1)
        self.assertEqual(find_majority_element_bayer_moore_method([0, 0, 1, 1, 0, 0]), 0)
        self.assertEqual(find_majority_element_bayer_moore_method([2, 2, 2, 3, 4]), 2)
        # self.assertEqual(find_majority_element_bayer_moore_method([2, 3, 7, 3, 4]), 0)


if __name__ == '__main__':
    unittest.main()
