"""
Maximum Sum Subarray

    Given a list of integers, find the sum of a non-empty subarray that has the largest sum.

    Examples:
        Input => "numbers": [2, -6, 3, 4, -5]
        Output => 7

        Input => "numbers": [-7, -9, -3, -5]
        Output => -3

    Note:
        A subarray is an array composed of a contiguous block of the original array's elements.
"""
import math


def maximum_sub_array_brute_force_three_loop(numbers: list[int]) -> int:
    """
    The most basic solution is to explore all possible sub-arrays (for all i and j, where i ≤ j),
    calculate the sum of each subarray and return the maximum among them.
    :param numbers: numbers to find maximum sub array
    :return: max sub array number
    """
    max_sum_sub_array = -math.inf
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            sum_sub_array = 0
            for k in range(i, j + 1):
                sum_sub_array += numbers[k]
            if sum_sub_array > max_sum_sub_array:
                max_sum_sub_array = sum_sub_array
    return max_sum_sub_array


def maximum_sub_array_brute_force_dual_loop(numbers: list[int]) -> int:
    """
    we can easily calculate the subarray sum from i to j + 1 in O(1),
    if we know the sub-array sum from i to j.
    Here is the formula: Subarray sum from i to j + 1 = Subarray sum from i to j + X[j + 1].
    :param numbers: numbers to find maximum sub array
    :return: max sub array number
    """
    max_sum_sub_array = -math.inf
    for i in range(0, len(numbers)):
        sum_sub_array = 0
        for j in range(i, len(numbers)):
            sum_sub_array += numbers[j]
            if sum_sub_array > max_sum_sub_array:
                max_sum_sub_array = sum_sub_array
    return max_sum_sub_array


def maximum_sub_array_neet_code_sample(numbers: list[int]) -> int:
    max_sum_sub_array = numbers[0]
    current_sum = 0
    for num in numbers:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        max_sum_sub_array = max(current_sum, max_sum_sub_array)
    return max_sum_sub_array


def maximum_sub_array_kadane_algorithm(numbers: list[int]) -> int:
    """
    Calculate the maximum subarray sum ending at the ith index using
    the maximum subarray sum ending at the (i - 1)th index.
    So, we can easily track this value for each index using a variable (maxSumEndingHere) in a single loop
    i.e. maxSumEndingHere = max(maxSumEndingHere + X[i], X[i]).
    The value of the maximum subarray sum will be the maximum of all subarray sums ending at index i.
    So, we can also track this value in a variable (maxSumSoFar) within the same loop
    i.e. if (maxSumEndingHere > maxSumSoFar), maxSumSoFar = maxSumEndingHere.

    :param numbers: numbers to find maximum sub array
    :return: max sub array number
    """
    max_sum_sub_array = numbers[0]
    max_ending = 0
    for num in numbers:
        max_ending = max(max_ending + num, num)
        if max_sum_sub_array < max_ending:
            max_sum_sub_array = max_ending
    return max_sum_sub_array
