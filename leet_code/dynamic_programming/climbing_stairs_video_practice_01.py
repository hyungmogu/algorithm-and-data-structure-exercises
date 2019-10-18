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
# Pseudocode

# def.__init__(self):
#     self.memo = {}

# def climbingStairs(self, steps, current_amount):
#     #   1. if base condition is satisfied (current_amount == 0), return the value of 1
#     if current_amount == 0:
#         return 1

#     #   2. if base condition is not satisfied (current_amount < 0), return the value of 0
#     if current_amount < 0:
#         return 0

#     if current_amount in self.memo:
#         return self.memo[current_amount]

#     #   3. use modified fibonacci programming to recursively explore all possible combinations of 1 and 2, and store it in variable called 'num_possible_paths'
#     num_possible_paths = 0
#     for variant in steps:
#         num_possible_paths += self.climbingStairs(steps, current_amount - variant)

#     self.memo[current_amount] = num_possible_paths

#     #   4. return num_possible_paths
#     return num_possible_paths


#                                  climbingStairs(steps, 2)
#                                         /               \
#                    climbingStairs(steps, 1)            climbingStairs(steps, 2)
#                            /   \                          /                   \
#  climbingStairs(stepts, 0)   climbingStairs(-1) climbingStairs(steps, 1)      climbingStairs(steps, 0)

class Solution:
    def __init__(self):
        self.memo = {}

    def climbingStairs(self, steps, current_amount):
        #   1. if base condition is satisfied (current_amount == 0), return the value of 1
        if current_amount == 0:
            return 1

        #   2. if base condition is not satisfied (current_amount < 0), return the value of 0
        if current_amount < 0:
            return 0

        if current_amount in self.memo:
            return self.memo[current_amount]

        #   3. use modified fibonacci programming to recursively explore all possible combinations of 1 and 2, and store it in variable called 'num_possible_paths'
        num_possible_paths = 0
        for variant in steps:
            num_possible_paths += self.climbingStairs(steps, current_amount - variant)

        self.memo[current_amount] = num_possible_paths

        #   4. return num_possible_paths
        return num_possible_paths


if __name__ == '__main__':
    case_1 = 2
    case_2 = 3
    case_3 = 0
    case_4 = 1

    steps_1 = [1, 2]
    steps_2 = [1, 2]
    steps_3 = [1, 2]
    steps_4 = [1, 2]

    expected_1 = 2
    expected_2 = 3
    expected_3 = 0
    expected_4 = 1

    solution_1 = Solution().climbingStairs(steps_1, case_1)
    solution_2 = Solution().climbingStairs(steps_2, case_2)
    solution_3 = Solution().climbingStairs(steps_3, case_3)
    solution_4 = Solution().climbingStairs(steps_4, case_4)

    assert expected_2 == solution_2