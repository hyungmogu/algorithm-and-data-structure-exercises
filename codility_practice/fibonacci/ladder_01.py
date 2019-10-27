# Ladder
#
# You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to
# N. With each step, you can ascend by one or two rungs. More precisely:
#
# with your first step you can stand on rung 1 or 2,
# if you are on rung K, you can move to rungs K + 1 or K + 2,
# finally you have to stand on rung N.
# Your task is to count the number of different ways of climbing to the top of the ladder.
#
# For example, given N = 4, you have five different ways of climbing, ascending by:
#
# 1, 1, 1 and 1 rung,
# 1, 1 and 2 rungs,
# 1, 2 and 1 rung,
# 2, 1 and 1 rungs, and
# 2 and 2 rungs.
# Given N = 5, you have eight different ways of climbing, ascending by:
#
# 1, 1, 1, 1 and 1 rung,
# 1, 1, 1 and 2 rungs,
# 1, 1, 2 and 1 rung,
# 1, 2, 1 and 1 rung,
# 1, 2 and 2 rungs,
# 2, 1, 1 and 1 rungs,
# 2, 1 and 2 rungs, and
# 2, 2 and 1 rung.
# The number of different ways can be very large, so it is sufficient to return the
# result modulo 2P, for a given integer P.
#
# Write a function:
#
# def solution(A, B)
#
# that, given two non-empty arrays A and B of L integers, returns an array consisting
# of L integers specifying the consecutive answers; position I should contain the
# number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].
#
# For example, given L = 5 and:
#
#     A[0] = 4   B[0] = 3
#     A[1] = 4   B[1] = 2
#     A[2] = 5   B[2] = 4
#     A[3] = 5   B[3] = 3
#     A[4] = 1   B[4] = 1
# the function should return the sequence [5, 1, 8, 0, 1], as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# L is an integer within the range [1..50,000];
# each element of array A is an integer within the range [1..L];
# each element of array B is an integer within the range [1..30].

# ===================== Solution ===============

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# problem: find all different possible of [1, 2] that sums to N
#
# input
#   - list of integers * 2 (A,B)
#
# output
#   - list of integers
#
# known
#   - the output is in format of 2** (B * index) where index represents index in A or B
#
# constraint
#   - L or size of list is in between [1 ... 50,000]
#   - each element of Array A is in between [1 ... L]
#   - each element of Array B is in between [1 ... 30]
#
#
#
# Brainstorming solution


class Solution:
    def solve(self, A, B):
        #   1. initialize L, and sequence (L = len(A), sequence = [None] * L)
        L = len(A)
        sequence = [None] * L
        index = 0

        #   2. get possibilities in between [1 ... L] and store in 'ways_of_climbing_dict'
        ways_of_climbing_dict = self.get_diff_ways_of_climbing(L)

        #   3. for each element and index in A,
        while index < len(A):
            #   4. get different possiblities of climbing given N = A[index], and
            #   5. store possibilities % 2 **(B[index] * index) to output 'sequence'
            modulo_by = 2**(B[index])
            sequence[index] = ways_of_climbing_dict[A[index]] % modulo_by
            #   6. return sequence
            index += 1

        return sequence
        # time complexity is O(N) and spatial complexity is O(N)

    def get_diff_ways_of_climbing(self, L):
        if L == 1:
            return [1]

        if L == 2:
            return [1,1]

        #   1. initialize dp = [0] * L and dp[0] = 1
        index_end = L + 1 # to include result of L in dp
        index = 2
        dp = [0] * index_end
        dp[0] = 1
        dp[1] = 1

        #   2. if L != 2, for each index in range(2,L+1),
        while index < index_end:
        #   3. evaluate dp[index] = dp[index-1] + dp[index-2]
            dp[index] = dp[index-1] + dp[index-2]
        #   return dp
            index += 1

        return dp

if __name__ == '__main__':
    A_case_1 = [4,4,5,5,1]
    B_case_1 = [3,2,4,3,1]

    expected_1 = [5,1,8,0,1]

    solution_1 = Solution().solve(A_case_1, B_case_1)

    assert expected_1 == solution_1