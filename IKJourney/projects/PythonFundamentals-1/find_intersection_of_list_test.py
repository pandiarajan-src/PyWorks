import unittest
from find_intersection_of_list import find_intersection_of_list_detailed, find_intersection_of_list_naive


class MyTestCase(unittest.TestCase):
    def test_intersection_of_list_success(self):
        self.assertListEqual([2, 2, 3], find_intersection_of_list_naive([4, 2, 2, 3, 1], [2, 2, 2, 3, 3]))
        self.assertListEqual([2, 2, 3], find_intersection_of_list_detailed([4, 2, 2, 3, 1], [2, 2, 2, 3, 3]))

        self.assertListEqual([], find_intersection_of_list_naive([6, 2, 4], [1, 5, 3, 7]))
        self.assertListEqual([], find_intersection_of_list_detailed([6, 2, 4], [1, 5, 3, 7]))

        self.assertListEqual([1], find_intersection_of_list_naive([1], [1]))
        self.assertListEqual([1], find_intersection_of_list_detailed([1], [1]))

        self.assertListEqual([], find_intersection_of_list_naive([-10, 100, 5, 2, 94, 13], [7, 7, 14, 92, 14, 92, 92]))
        self.assertListEqual([],
                             find_intersection_of_list_detailed([-10, 100, 5, 2, 94, 13], [7, 7, 14, 92, 14, 92, 92]))

        self.assertListEqual([1], find_intersection_of_list_naive([1], [1]))
        self.assertListEqual([1], find_intersection_of_list_detailed([1], [1]))


if __name__ == '__main__':
    unittest.main()
