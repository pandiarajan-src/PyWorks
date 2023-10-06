import unittest
from insert_element_at_position import insert_element_at_position


class TestInsertElements(unittest.TestCase):

    def test_insert_element_at_position_success(self):
        self.assertListEqual([2, 3, 4, 5, 6], insert_element_at_position([2, 4, 5, 6, -1], 3, 2))
        self.assertListEqual([70, 60, 50, 40], insert_element_at_position([70, 60, 50, -1], 40, 4))
        self.assertListEqual([10, 100, 5, 70, 35, 27, 64],
                             insert_element_at_position([100, 5, 70, 35, 27, 64, -1], 10, 1))
        self.assertListEqual([25, 13], insert_element_at_position([13, -1], 25, 1))


if __name__ == '__main__':
    unittest.main()
