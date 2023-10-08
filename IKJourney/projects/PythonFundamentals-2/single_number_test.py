import unittest
from single_number import find_single_number_naive, \
    find_single_number_using_set, find_single_number_using_list_add_remove


class TestSingleNumer(unittest.TestCase):
    def test_single_number_naive(self):
        self.assertEqual(find_single_number_naive([2, 1, 2, 5, 1]), 5)
        self.assertEqual(find_single_number_naive([1000000000]), 1000000000)
        self.assertEqual(find_single_number_naive([-1000000000, 0, 0, -1000000000, 10]), 10)
        self.assertEqual(find_single_number_naive([1, 3, 1]), 3)
        self.assertEqual(find_single_number_naive([1, 1, 3]), 3)
        self.assertEqual(find_single_number_naive([3, 1, 1]), 3)
        self.assertEqual(find_single_number_naive([-9, 10, 4, -9, 6, 10, 4]), 6)
        self.assertEqual(find_single_number_naive([1, 1, 0, -1000000000, 0, 3, 3]), -1000000000)
        self.assertEqual(find_single_number_naive([1, 1, 2, 2, 5, 5, 6, 10, 10]), 6)
        self.assertEqual(find_single_number_naive([10, 10, 9, 9, 8, 8, 7, 0, 0]), 7)

    def test_find_single_number_using_set(self):
        self.assertEqual(find_single_number_using_set([2, 1, 2, 5, 1]), 5)
        self.assertEqual(find_single_number_using_set([1000000000]), 1000000000)
        self.assertEqual(find_single_number_using_set([-1000000000, 0, 0, -1000000000, 10]), 10)
        self.assertEqual(find_single_number_using_set([1, 3, 1]), 3)
        self.assertEqual(find_single_number_using_set([1, 1, 3]), 3)
        self.assertEqual(find_single_number_using_set([3, 1, 1]), 3)
        self.assertEqual(find_single_number_using_set([-9, 10, 4, -9, 6, 10, 4]), 6)
        self.assertEqual(find_single_number_using_set([1, 1, 0, -1000000000, 0, 3, 3]), -1000000000)
        self.assertEqual(find_single_number_using_set([1, 1, 2, 2, 5, 5, 6, 10, 10]), 6)
        self.assertEqual(find_single_number_using_set([10, 10, 9, 9, 8, 8, 7, 0, 0]), 7)

    def test_find_single_number_using_list_add_remove(self):
        self.assertEqual(find_single_number_using_list_add_remove([2, 1, 2, 5, 1]), 5)
        self.assertEqual(find_single_number_using_list_add_remove([1000000000]), 1000000000)
        self.assertEqual(find_single_number_using_list_add_remove([-1000000000, 0, 0, -1000000000, 10]), 10)
        self.assertEqual(find_single_number_using_list_add_remove([1, 3, 1]), 3)
        self.assertEqual(find_single_number_using_list_add_remove([1, 1, 3]), 3)
        self.assertEqual(find_single_number_using_list_add_remove([3, 1, 1]), 3)
        self.assertEqual(find_single_number_using_list_add_remove([-9, 10, 4, -9, 6, 10, 4]), 6)
        self.assertEqual(find_single_number_using_list_add_remove([1, 1, 0, -1000000000, 0, 3, 3]), -1000000000)
        self.assertEqual(find_single_number_using_list_add_remove([1, 1, 2, 2, 5, 5, 6, 10, 10]), 6)
        self.assertEqual(find_single_number_using_list_add_remove([10, 10, 9, 9, 8, 8, 7, 0, 0]), 7)


if __name__ == '__main__':
    unittest.main()
