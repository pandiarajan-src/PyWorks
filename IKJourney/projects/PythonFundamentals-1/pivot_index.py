# region Get Pivot Index
# Find Pivot Index
# Given a list of integers numbers, calculate the pivot index of this list.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index
#       is equal to the sum of all the numbers strictly to the index's right.
#       If the index is on the left edge of the array,
#       then the left sum is 0 because there are no elements to the left.
#       This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.
#
# Example
#   Input => "numbers": [2, 3, 1, -1, 1, 1, 4]
#   Output => 2
#
#   Input => "numbers": [2, 3, 5]
#   Output => -1
#
def get_pivot_index(nums: list) -> int:
    for index in range(len(nums)):
        if sum(nums[:index]) == sum(nums[index+1:]):
            return index
    return -1

# endregion
