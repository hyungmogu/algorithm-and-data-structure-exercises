# Number Solitaire
#
# given an array of integers A, find the maximum possible value at position
# N-1 (N is the size of A) given that 6 possible moves can be made
# {move 1, move 2, move 3, move,4 move 5, move 6}
#
#
# input
#   - list of integers
# output
#   - integer (highest sum that can be achieved)
#
# Known
#   - 6 possible moves can be made / position
#
# Constraint
#   - Size N is in between [2 ... 100,000]
#   - element in Array A has value in between [-10,000 ... 10,000]
#
# Example
# [1,-2,0,9,-1,-2]
#
#
# output: 8
#
#
#
# A = [1,-2] --> highest sum at N-1 = -1 -->   dp = [1,-1]
#
#
# A = [1,-2,0] --> highest sum N-1 = 1 --> dp = [1,-1,1] --> maybe max(dp[:index]) + A[index]
#
# A = [1,-2,0,9] --> highest sum N-1 = 10 --> dp = [1,-1,1,10] --> hey! max(dp[:index]) + A[index]
#
# A = [1,-2,0,9,-1] --> highest sum N-1 = 9 --> dp = [1,-1,1,10,9] --> max(dp[:index]) + A[index]

# A = [1,-2,0,9,-1,-2] --> highest sum N-1 = 8 --> dp = [1,-1,1,10,9,8] --> max(dp[:index]) + A[index]
#
#
# let's say N = 20 --> max(dp[index - 6:index]) + A[index]
#
#
# brainstorming solution
#
#   1. initialize dp
#   2. find values of dp for first 6 moves
#   3. find values of dp for remaining moves if exist
#   4. return dp[-1]
#
# time complexity O(N), spatial complexity O(N)
#
# cases
#   1. len(A) == 2
#   2. len(A) > 2 but less than 7
#   3. len(A) > 7

class Solution:
    def solve(self, A):

        if len(A) == 2:
            return sum(A)

        N = len(A)
        #   1. initialize dp
        dp = [A[0]] + [0] * (N - 1)

        index_dice = 1
        index = 7
        #   2. find values of dp for first 6 moves
        while index_dice < min(7,N):
            dp[index_dice] = max(dp[:index_dice]) + A[index_dice]
            index_dice += 1

        #   3. find values of dp for remaining moves if exist
        while index < N:
            dp[index] = max(dp[index - 6: index]) + A[index]
            index += 1

        #   4. return dp[-1]
        return dp[-1]


if __name__ == '__main__':
    A_case_1 = [1,2]
    A_case_2 = [1,-2,0,9,-1,-2]

    expected_1 = 3
    expected_2 = 8

    solution_1 = Solution().solve(A_case_1)
    solution_2 = Solution().solve(A_case_2)

    assert expected_1 == solution_1
    assert expected_2 == solution_2