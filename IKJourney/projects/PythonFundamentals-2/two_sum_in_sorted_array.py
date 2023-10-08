"""
Two Sum in a Sorted Array

Given an array sorted in non-decreasing order and a target number,
find the indices of the two values from the array that sum up to the given target number.

Example:
    Input:
        {
        "numbers": [1, 2, 3, 5, 10],
        "target": 7
        }
    Output:
        [1, 3]

In case when no answer exists, return an array of size two with both values equal to -1, i.e., [-1, -1].
In case when multiple answers exist, you may return any of them.
The order of the indices returned does not matter.
A single index cannot be used twice.
"""


def pair_sum_sorted_array_normal_case(numbers, target):
    if len(numbers) < 2:
        return []
    for index in range(len(numbers)):
        try:
            pair_pos = numbers.index(target - numbers[index])
        except ValueError:
            continue

        if pair_pos != index:
            return [index, pair_pos]
    return [-1, -1]


def pair_sum_sorted_array_two_pointers(numbers, target):
    """
        Have two pointers left and right move both the pointer left and right until get the target
        :param numbers: list of numbers to find the target
        :param target: target number to check
        :return: tuple of indexes that adds the sum of target
    """
    if len(numbers) < 2:
        return [-1, -1]
    left_index = 0
    right_index = len(numbers) - 1
    while left_index < right_index:
        if numbers[left_index] + numbers[right_index] > target:
            right_index -= 1
        elif numbers[left_index] + numbers[right_index] < target:
            left_index += 1
        else:  # numbers[left_index] + numbers[right_index] == target
            return [left_index, right_index]
    return [-1, -1]
