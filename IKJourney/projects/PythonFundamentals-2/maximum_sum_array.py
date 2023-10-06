import math

# def find_maximum_sum_subarray(numbers):
#     """
#     Args:
#      numbers(list_int32)
#     Returns:
#      int32
#     """
#     # Write your code here.
#     max_sum = -math.inf
#     length = len(numbers)
#     for outer_index in range(length):
#         for inner_index in range(length):
#             # if outer_index == inner_index:
#             #     continue
#             temp_sum = numbers[outer_index] + numbers[inner_index]
#             print(f"numbers[{outer_index}] ({numbers[outer_index]}) + "
#                   f"numbers[{inner_index}]({numbers[inner_index]}) = {temp_sum}")
#             if temp_sum > max_sum:
#                 max_sum = temp_sum
#     return max_sum


def find_maximum_sum_subarray(numbers):
    """
    Args:
     numbers(list_int32): A list of integers.
    Returns:
     int32: The maximum sum of any subarray in the input list.
    """
    max_subarray = -math.inf
    for i in range(len(numbers)):
        current_subarray = 0
        for j in range(i, len(numbers)):
            current_subarray += numbers[j]
            max_subarray = max(max_subarray, current_subarray)

    return max_subarray


print(find_maximum_sum_subarray([-7, -9, -3, -5]))
