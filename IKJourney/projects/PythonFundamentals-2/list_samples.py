# region Two Sum In A sorted Array
#
# 2 Sum In A Sorted Array
#
# Given an array sorted in non-decreasing order and a target number,
# find the indices of the two values from the array that sum up to the given target number.
#
# Examples
#   Input => "numbers": [1, 2, 3, 5, 10],  "target": 7
#   Output => [1, 3]
#
# Notes
#   In case when no answer exists,
#           return an array of size two with both values equal to -1, i.e., [-1, -1].
#   In case when multiple answers exist, you may return any of them.
#   The order of the indices returned does not matter.
#   A single index cannot be used twice.
#
#
def pair_sum_sorted_array(numbers: list, target: int) -> list:
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    for index in range(len(numbers)):
        try:
            pos = numbers.index((target - numbers[index]), (index + 1), len(numbers))
        except ValueError:
            continue
        return [index, pos]
    return [-1, -1]

# endregion