# Number Solitaire
#
# A game for one player is played on a board consisting of N consecutive squares,
# numbered from 0 to N − 1. There is a number written on each square. A non-empty
# array A of N integers contains the numbers written on the squares. Moreover,
# some squares can be marked during the game.

# At the beginning of the game, there is a pebble on square number 0 and this is
# the only square on the board which is marked. The goal of the game is to move
# the pebble to square number N − 1.

# During each turn we throw a six-sided die, with numbers from 1 to 6 on its
# faces, and consider the number K, which shows on the upper face after the die
# comes to rest. Then we move the pebble standing on square number I to square
# number I + K, providing that square number I + K exists. If square number I + K
# does not exist, we throw the die again until we obtain a valid move. Finally,
# we mark square number I + K.

# After the game finishes (when the pebble is standing on square number N − 1),
# we calculate the result. The result of the game is the sum of the numbers
# written on all marked squares.

# For example, given the following array:

#     A[0] = 1
#     A[1] = -2
#     A[2] = 0
#     A[3] = 9
#     A[4] = -1
#     A[5] = -2
# one possible game could be as follows:

# the pebble is on square number 0, which is marked;
# we throw 3; the pebble moves from square number 0 to square number 3; we mark
# square number 3;
# we throw 5; the pebble does not move, since there is no square number 8 on the board;
# we throw 2; the pebble moves to square number 5; we mark this square and the game ends.
# The marked squares are 0, 3 and 5, so the result of the game is 1 + 9 + (−2) = 8.
# This is the maximal possible result that can be achieved on this board.

# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the maximal result that
# can be achieved on the board represented by array A.

# For example, given the array

#     A[0] = 1
#     A[1] = -2
#     A[2] = 0
#     A[3] = 9
#     A[4] = -1
#     A[5] = -2
# the function should return 8, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].
#
#
# =============== Solution =================
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# Goal: return maximal result that can be achieved on th board
# represented by array A

#
# constraints
#   - N is integer in range [2 ... 100,000]
#   - each element in Array [-10,000, 10,000]
#   - K is in range [1 ... 6]
#
# [1] -> [1]
#
# [1, -2] -> [1, -1]
#
# [1, -2, 0] -> [1, -1, 1] --> hey ! this is just max(dp[:index]) + A[index]
#
# [1, -2, 0, 9] -> [1, -1, 1, 10] --> hey! again this is just max(dp[:index]) + A[index]
#
# [1, -2, 0, 9, -1] -> [1,-1,1,10,9] -> max(dp[:index]) + A[index]
#
# [1, -2, 0, 9, -1, -2] -> [1,-1,1,10,9,8] -> max(dp[:index]) + A[index]
#
# pseudocode
#   1. initialize dp array (dp = [A[0]] + [0] * (N - 1) )
#   2. find dp of first 6 steps given A
#   3. use dp of first 6 steps to find value till A[N-1]
#   4. return dp[-1]
#
# time compexity of O(N) and spatial complexity of O(N)

# case
#   1. N == 2
#   2. N != 2 and N <= 7
#   3. N > 6

class Solution:
    def solve(self, A):
        #   1. initialize dp array (dp = [A[0]] + [0] * (N - 1) )
        if len(A) == 2:
            return sum(A)

        N = len(A)
        dp = [A[0]] + [0] * (N-1)

        index_dice = 1
        index = 7

        #   2. find dp of first 6 steps given A
        while index_dice < min(7, N):
            dp[index_dice] = max(dp[:index_dice]) + A[index_dice]
            index_dice += 1

        #   3. use dp of first 6 steps to find value till A[N-1]
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

    solution_1 = Solution().solve(A_case1)
    solution_2 = Solution().solve(A_case2)

    assert expected_1 == solution_1
    assert expected_2 == solution_2