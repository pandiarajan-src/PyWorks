"""
Squares Of A Sorted Array

    Given an array of numbers sorted in increasing order,
    generate another array containing the square of all the elements in the given array, sorted in increasing order.

    Example:
        Input => [1, 2, 3, 4]
        Output => [1, 4, 9, 16]

         Input => [-9, -5, -2, 0, 3, 7]
        Output => [0, 4, 9, 25, 49, 81]
"""


def squares_of_a_sorted_array_naive(numbers: list[int]) -> list[int]:
    return sorted([pow(num, 2) for num in numbers])


