from math import floor


def majority_element(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    nums_count_dict = dict()
    for num in nums:
        if num in nums_count_dict:
            nums_count_dict[num] += 1
        else:
            nums_count_dict[num] = 1
    print(nums_count_dict)
    for num, num_count in nums_count_dict.items():
        if num_count >= floor(len(nums) / 2):
            return num
    return 0


def get_intersection(numbers1, numbers2):
    """
    Args:
     numbers1(list_int32)
     numbers2(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    s1 = set(numbers1)
    s2 = set(numbers2)
    result = list(s1.intersection(s2))
    if len(result) == 0:
        return [-1]
    else:
        return result


def single_number(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    print(arr)
    arr.sort()
    print(arr)
    for index in range(0, len(arr), 2):
        if index == len(arr)-1:
            return arr[index]
        if arr[index] != arr[index+1]:
            return arr[index]
    return 0

di = dict()
di.popitem()

print(single_number([2, 1, 2, 5, 1]))

# print(get_intersection([1, 2, 2, 6, 7], [2, 2, 7, 7]))
# print(get_intersection([5, 9, 11],  [1, 4, 10, 12]))

# print(majority_element([3, 3, 3, 2, 4, 4, 3, 3, 3]))