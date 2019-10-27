# Max Profit
#
# Given an array A of integers, find the maximum profit that can be made
# by buying stock at index_P in A and selling at index_Q.
#
# stock can be bought and sold on the same day as long as this order is maintained
# (0 ≤ index_P ≤ index_Q < N)
#
# if no profit can be made, return value 0
#
#
# input
#   - list of integers
# output
#   - integer
#
# constraint
#   - size N is in between [0 ... 400,000]
#   - each element in A is in between [0 ... 200,000]
#
#   - if no profit can be found return 0
#
# Example
#
# [23171, 21011, 21123, 21366, 21013, 21367]
#           P                            Q
#
#
# output: 356 --> if it was bought at P and sold at Q, then max profit can be made
#
#
# cases
#   1. len(A) == 0, --> return 0
#   2. len(A) == 1 --> return 0
#   3. len(A) != 1
#
#
# brainstorming - brute force
#
# [23171, 21011, 21123, 21366, 21013, 21367]
#   - examine all possibilities and return the highest price
#       - for each element and index_p in A and nested for loop element and index_q in A,
#           1. if index_q < index_p, then continue
#           2. calculate the price between index_Q and index_P current_profit
#           3. compare with the current highest 'max_profit', and set max_profit = current_profit
#
#           4. return result
#
#   time complexity O(N^2) spatial complexity of O(1)
#
# improved solution (greedy --> just by adding something we will somehow get to result --> time complexity O(N) and spatial complexity O(1))
#
# [23171, 21011, 21123, 21366, 21013, 21367] --> [-2160, 112, 243, -353, 354] (this is what we are going to use for greedy)
#
#   1. for each element in A with index starting at 1
#   2. determine current profit (current_profit = A[index] - A[index-1])
#   3. find local maximum 'max_ending' (max_ending = max(0, max_ending + current_profit))
#   4. find global maximum 'max_slice' (max_slice = max(max_ending, max_slice))
#
#   5. return max_slice
class Solution:
    def solve(self, A):

        if len(A) == 0 or len(A) == 1:
            return 0

        max_ending = 0
        max_slice = 0
        index = 1

        #   1. for each element in A with index starting at 1
        while index < len(A):
            #   2. determine current profit (current_profit = A[index] - A[index-1])
            current_profit = A[index] - A[index - 1]

            #   3. find local maximum 'max_ending' (max_ending = max(0, max_ending + current_profit))
            max_ending = max(0, max_ending + current_profit)

            #   4. find global maximum 'max_slice' (max_slice = max(max_ending, max_slice))
            max_slice = max(max_ending, max_slice)

            index += 1
        #
        #   5. return max_slice
        return max_slice

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

