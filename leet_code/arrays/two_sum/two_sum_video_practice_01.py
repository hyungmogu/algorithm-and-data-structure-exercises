# Two Sum (10/06/2019)
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# input: nums = [2, 7, 11, 15] (list of integers), target = 9 (integer),
# output: [0,1] Because nums[0] + nums[1] = 2 + 7 = 9 (list of integers),
#
#
#
#
# Constraints
#   1. pair of indexes where its value sum to target are unique
#   2. same element cannot be used twice
#
#
#
# Brute Force solution
#
# [2, 7, 11, 15]
#  x
#             ^
#
# [11, 7, 15, 2]
#      x
#             ^
#
# [1, 3]
#
class Solution():
    def twoSum(self, nums, target):
        #
        # 1. for pointer i in nums
        # 2. for pointer j in nums
        for index_i, value_i in enumerate(nums):
            for index_j, value_j in enumerate(nums):

                #
                # 3. if i == j, continue
                if index_i == index_j:
                    continue
                # 4. if i != j, and nums[i] == nums[j], return [i,j]
                if index_i != index_j and value_i + value_j == target:
                    return [index_i, index_j]


if __name__ == '__main__':
    nums_1 = [2, 7, 11, 15]
    nums_2 = [11, 7, 15, 2]

    target = 9

    expected_1 = [0,1]
    expected_2 = [1,3]

    solution_1 = Solution().twoSum(nums_1, target)
    solution_2 = Solution().twoSum(nums_2, target)

    print(solution_1)

    assert solution_1 == expected_1
    assert solution_2 == expected_2



