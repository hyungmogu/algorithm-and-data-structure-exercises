# Two Sum

# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#  ==================== Solution ==================
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers_index_dict = {}

        for (index, value) in enumerate(nums):

            if value not in numbers_index_dict:
                numbers_index_dict[value] = [index]
            else:
                numbers_index_dict[value].append(index)

        for (index, value) in enumerate(nums):
            required_value = target - value

            if ((required_value in numbers_index_dict) and (required_value != value) or
                (required_value in numbers_index_dict) and (required_value == value) and (len(numbers_index_dict[required_value]) > 1)):
                solution = [index, numbers_index_dict[required_value][-1]]
                solution.sort()

                return solution

