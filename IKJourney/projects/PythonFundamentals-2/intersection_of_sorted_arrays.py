"""
Intersection Of Two Sorted Arrays

    Given two integer arrays sorted in non-decreasing order, find the intersection of both the arrays.

    Example:
        input =>
            "numbers1": [1, 2, 2, 6, 7],
            "numbers2": [2, 2, 7, 7]
        output => [2, 7]
        2 and 7 are present in both the given arrays.

        input =>
            "numbers1": [5, 9, 11],
            "numbers2": [1, 4, 10, 12]
        output => [-1]

    Note:
        Intersection should be free of duplicates and sorted in ascending order.
        If there is no element common in both the arrays, return [-1].
"""


def intersection_of_two_sorted_array(numbers1: list[int], numbers2: list[int]) -> list[int]:
    """
    Find the intersection of two sorted array by converting the list to set
    :param numbers1: list of numbers1
    :param numbers2: list of numbers2
    :return: list of intersection of sorted array, else return list[-1]
    """
    result = list(set(numbers1).intersection(set(numbers2)))
    return result if len(result) > 0 else [-1]


def intersection_of_two_sorted_array_naive(numbers1: list[int], numbers2: list[int]) -> list[int]:
    """
    Find the intersection of two sorted array by native method
    :param numbers1: list of numbers1
    :param numbers2: list of numbers2
    :return: list of intersection of sorted array, else return list[-1]
    """

    result = {num for num in numbers1 if num in numbers2}
    # Alternative expansion
    # for num1 in numbers1:
    #     if num1 in numbers2:
    #         result.add(num1)
    return list(result) if len(result) > 0 else [-1]
