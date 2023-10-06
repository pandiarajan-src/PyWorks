import unittest
from reverse_an_array import reverse_array_simplified, reverse_array_complex


class ReverseAnArrayTestCase(unittest.TestCase):
    def test_reverse_array_success(self):
        self.assertListEqual([5, 4, 3, 2, 1], reverse_array_simplified([1, 2, 3, 4, 5]))
        self.assertListEqual([5, 4, 3, 2, 1], reverse_array_complex([1, 2, 3, 4, 5]))

        self.assertListEqual([17, 66, 78, 35, 50], reverse_array_simplified([50, 35, 78, 66, 17]))
        self.assertListEqual([17, 66, 78, 35, 50], reverse_array_complex([50, 35, 78, 66, 17]))

        self.assertListEqual([20, 30, 40, 50], reverse_array_simplified([50, 40, 30, 20]))
        self.assertListEqual([20, 30, 40, 50], reverse_array_complex([50, 40, 30, 20]))

        self.assertListEqual([100, 200, 300, 300, 200, 100], reverse_array_simplified([100, 200, 300, 300, 200, 100]))
        self.assertListEqual([100, 200, 300, 300, 200, 100], reverse_array_complex([100, 200, 300, 300, 200, 100]))

        self.assertListEqual([134, 198, 278, 457, 20, 457, 278, 198, 134],
                             reverse_array_simplified([134, 198, 278, 457, 20, 457, 278, 198, 134]))
        self.assertListEqual([134, 198, 278, 457, 20, 457, 278, 198, 134],
                             reverse_array_complex([134, 198, 278, 457, 20, 457, 278, 198, 134]))

        self.assertListEqual([557, 557, 557, 557, 557, 557, 557, 557, 557, 557, 557],
                             reverse_array_simplified([557, 557, 557, 557, 557, 557, 557, 557, 557, 557, 557]))
        self.assertListEqual([557, 557, 557, 557, 557, 557, 557, 557, 557, 557, 557],
                             reverse_array_complex([557, 557, 557, 557, 557, 557, 557, 557, 557, 557, 557]))

        self.assertListEqual([4580], reverse_array_simplified([4580]))
        self.assertListEqual([4580], reverse_array_complex([4580]))

        self.assertListEqual([], reverse_array_simplified([]))
        self.assertListEqual([], reverse_array_complex([]))

    def test_reverse_array_failure(self):
        self.assertNotEqual([5, 4, 3, 2, 1], reverse_array_simplified([1, 2, 5, 4, 3]))
        self.assertNotEqual([5, 4, 3, 2, 1], reverse_array_complex([1, 2, 5, 4, 3]))


if __name__ == '__main__':
    unittest.main()
