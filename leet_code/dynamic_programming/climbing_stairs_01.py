# Climbing Stairs
#
#You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# Now this is a classic example of dynamic programming!! --> exploring all possible combinations
#   - here the base case is when
#
#
# Pseudocode
# def climbingStairs(self, total_sum, target_sum)
#     #   1. if the total amount is equal to input amount, return 1` (base case, success)
#     if total_sum == target_sum:
#         return 1

#     #   2. if the total amount is greater than the input amount, return 0 (base case, failure)
#     if total_sum > target_sum:
#         return 0

#     num_possible_paths = 0
#     #   3. return sum of all recursions from 1 to n-1 (this explores all possibilities of these integers)
#     for variant in range(1, target_sum):
#         num_possible_paths += self.climbingStairs(self, total_sum - variant, target_sum)

#     return num_possible_paths

class Solution:
    def climbingStairs(self, steps, current_amount):
        #   1. if the total amount is equal to input amount, return 1` (base case, success)
        if current_amount == 0:
            return 1

        #   2. if the total amount is greater than the input amount, return 0 (base case, failure)
        if current_amount < 0:
            return 0

        num_possible_paths = 0
        #   3. return sum of all recursions from 1 to n-1 (this explores all possibilities of these integers)
        for variant in steps:
            num_possible_paths += self.climbingStairs(steps, current_amount - variant)

        return num_possible_paths

if __name__ == '__main__':
    case_1 = 2
    case_2 = 3

    steps_1 = [1, 2]
    steps_2 = [1, 2]

    expected_1 = 2
    expected_2 = 3

    solution_1 = Solution().climbingStairs(steps_1, case_1)
    solution_2 = Solution().climbingStairs(steps_2, case_2)

    assert expected_2 == solution_2