# region Insert element at a given index
####################################################
# Given an array of numbers, insert a given element at the specified position in the array.
# Example => Input: "nums": [2, 4, 5, 6, -1], "element": 3, "position": 2
#            Output => [2, 3, 4, 5, 6]
# Notes:
#   1. The last element of the array is -1 indicating a blank position.
#   2. The given position follows 1-based indexing.
#   3. Return the modified array.

def insert_element_at_position(nums: list, element: int, position: int) -> list:
    """
    insert an element at a position
    :param nums: list
    :param element: int
    :param position: int
    :return: list
    """
    nums.insert(position-1, element)
    nums.pop()
    return nums

####################################################
# endregion