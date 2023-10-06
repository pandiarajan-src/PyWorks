# region Reverse an Array
##############################################################
# Reverse a given list of numbers.
# Example : Input => "nums": [50, 35, 78, 66, 17] Result => [17, 66, 78, 35, 50]
# Notes:
#   1. Modify the input array in-place and return the modified array.

# Time complexity O(n)
# Space complexity O(n)
def reverse_array_simplified(lst: list) -> list:
    """
    Reverse an Array with built-in simplified method
    :param lst: list
    :return: list
    """
    lst.reverse()
    return lst


# Time complexity O(n)
# Space complexity O(n)
def reverse_array_complex(nums: list) -> list:
    """
    own implementation of reverse an array
    :param nums: list
    :return: list
    """
    new_nums = []
    for index in reversed(range(len(nums))):
        new_nums.append(nums[index])
    return new_nums


##############################################################
# endregion
