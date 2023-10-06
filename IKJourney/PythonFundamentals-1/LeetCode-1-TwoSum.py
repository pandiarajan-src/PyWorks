# 1. Two Sum

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    @staticmethod
    def naive_two_sum(nums: list[int],
                      target: int
                      ) -> list[int]:
        nums_length = len(nums)
        if nums_length < 2:
            return []
        for i in range(nums_length):
            for j in range(i, nums_length):
                if (i != j) and (nums[i] + nums[j]) == target:
                    return [i, j]
        return []

    @staticmethod
    def optimized_two_sum(nums: list[int], target: int) -> list[int]:
        nums_length = len(nums)
        if nums_length < 2:
            return []
        for index in range(nums_length):
            try:
                pos = nums.index(target - nums[index])
            except ValueError:
                continue
            if pos != index:
                return [index, pos]
        return []


# print(Solution.naive_two_sum([2, 7, 11, 15], 9))
# print(Solution.naive_two_sum([3, 2, 4], 6))
# print(Solution.naive_two_sum([3, 3], 6))

print(Solution.optimized_two_sum([2, 7, 11, 15], 9))
print(Solution.optimized_two_sum([3, 2, 4], 6))
print(Solution.optimized_two_sum([3, 3], 6))
print(Solution.optimized_two_sum([], 6))
print(Solution.optimized_two_sum([1, 2, 3, 4], 25))




