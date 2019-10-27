# Max Profit
#
# An array A consisting of N integers is given. It contains daily prices of a stock
# share for a period of N consecutive days. If a single share was bought on day P
# and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is
# equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings
# loss of A[P] − A[Q].

# For example, consider the following array A consisting of six elements such that:

#   A[0] = 23171
#   A[1] = 21011
#   A[2] = 21123
#   A[3] = 21366
#   A[4] = 21013
#   A[5] = 21367
# If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur
# because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and
# sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354.
# Maximum possible profit was 356. It would occur if a share was bought on day 1
# and sold on day 5.

# Write a function,

# class Solution { public int solution(int[] A); }

# that, given an array A consisting of N integers containing daily prices of a stock
# share for a period of N consecutive days, returns the maximum possible profit from
# one transaction during this period. The function should return 0 if it was impossible
# to gain any profit.

# For example, given array A consisting of six elements such that:

#   A[0] = 23171
#   A[1] = 21011
#   A[2] = 21123
#   A[3] = 21366
#   A[4] = 21013
#   A[5] = 21367
# the function should return 356, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..400,000];
# each element of array A is an integer within the range [0..200,000].


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# problem: return the maximum possible profit from one transaction (buy and sell)
#
# Return 0 if profit cannot be made
#
# input
#   - list of integers (size N in between [0 ... 400,000])
#
# output
#   - integer (maximum profit in one transaction)
#
# constraint
#   - Size of A, N is in between [0 ... 400,000]
#   - each element in A is in between [0 ... 200,000]
#   - can be bought once and sold once
#
# Known
#   - 0 <= P <= Q
#   - profit = A[Q] - A[P]
#       - P => index of when share was purchased
#       - Q => index of when share was sold
#   - A[Q] - A[P] >= 0 --> profit
#   - A[Q] - A[p] < 0 --> loss
#
#
# Example
#
# #1
# [23171, 21011, 21123, 21366, 21013, 21367]
#
# #2
# [23171, 21011, 21123, 21366, 21013, 21367]
#    x      ^
#
#
# output: 356
#   -> when it's bought on day 1 and sold on day 5
#
# This is a classic maximum slice problem
#
# cases
#   1. len(A) == 0 <- return 0
#   2. len(A) == 1 <- return 0
#   3. len(A) != 1

# brute force solution
#   1. for each index_P and element in A, and nested for loop index_Q and element in A
#       1.1 if index_Q <= index_P, continue
#       1.2 find current_profit (A[index_Q] - A[index_P])
#       1.3 if current_profit > max_profit, max_profit = current_profit
#           and index_Q_max = index_Q and index_P_max = index_P
#   2.return max_profit
#
#   Time complexity O(N^2) and spatial complexity of O(1)
#
#
# Improvement --> using greey algorithm
# [23171, 21011, 21123, 21366, 21013, 21367]
#           x
# [-2160, 112, 243, -353, 354]
#    0
#    0
#
# [23171, 21011, 21123, 21366, 21013, 21367]
#                  x
# [-2160, 112, 243, -353, 354]
#         112
#         122
#
# [23171, 21011, 21123, 21366, 21013, 21367]
#                        x
# [-2160, 112, 243, -353, 354]
#                         355
#                         355
#
#
#   1.for each element in in A
#   2. calculate 'max_ending'
#   3. compare max_ending with 'max_slice'. if max_ending > max_slice, set max_slice = max_ending
#
#   4. return max_profit
#
## time complexity of O(N) and spatial complexity of O(1)

class Solution:
    def solve(self, A):
        #   1.for each element in in A
        if len(A) == 0 or len(A) == 1:
            return 0

        max_ending = 0
        max_slice = 0
        index = 1
        while index < len(A):
            revenue = A[index] - A[index - 1]

            #   2. calculate 'max_ending'
            max_ending = max(0, max_ending + revenue)

            #   3. compare max_ending with 'max_slice'. if max_ending > max_slice, set max_slice = max_ending
            max_slice = max(max_ending, max_slice)

            #   4. return max_profit
            index += 1

        return max_slice

        ## time complexity of O(N) and spatial complexity of O(1)

if __name__ == '__main__':
    case_1 = [23171, 21011, 21123, 21366, 21013, 21367]
    case_2 = []
    case_3 = [1]

    expected_1 = 356
    expected_2 = 0
    expected_3 = 0

    solution_1 = Solution().solve(case_1)
    solution_2 = Solution().solve(case_2)
    solution_3 = Solution().solve(case_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3


