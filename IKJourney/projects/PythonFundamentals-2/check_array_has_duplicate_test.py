import unittest
from check_array_has_duplicate import check_array_has_duplicate_native, \
    check_array_has_duplicate


class TestArrayHasDuplicates(unittest.TestCase):
    def test_check_array_has_duplicate(self):
        self.assertEqual(check_array_has_duplicate([10, 30, 10, 20]), True)
        self.assertEqual(check_array_has_duplicate([5, 10, 15, 20]), False)
        self.assertEqual(check_array_has_duplicate([1000, 1000, 1000, 1000, 1000, 1000]), True)
        self.assertEqual(check_array_has_duplicate([220]), False)
        self.assertEqual(check_array_has_duplicate([100, 90, 80, 70, 60, 50, 40]), False)
        self.assertEqual(check_array_has_duplicate([55, 11, 44, 11, 33, 55, 44, 22, 33, 55]), True)
        self.assertEqual(check_array_has_duplicate([250, 290, 230, 290, 245, 220, 263, 278]), True)

    def test_check_array_has_duplicate_native(self):
        self.assertEqual(check_array_has_duplicate_native([10, 30, 10, 20]), True)
        self.assertEqual(check_array_has_duplicate_native([5, 10, 15, 20]), False)
        self.assertEqual(check_array_has_duplicate_native([1000, 1000, 1000, 1000, 1000, 1000]), True)
        self.assertEqual(check_array_has_duplicate_native([220]), False)
        self.assertEqual(check_array_has_duplicate_native([100, 90, 80, 70, 60, 50, 40]), False)
        self.assertEqual(check_array_has_duplicate_native([55, 11, 44, 11, 33, 55, 44, 22, 33, 55]), True)
        self.assertEqual(check_array_has_duplicate_native([250, 290, 230, 290, 245, 220, 263, 278]), True)


if __name__ == '__main__':
    unittest.main()
