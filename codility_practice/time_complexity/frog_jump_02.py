# Frog Jump
# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
#
# A small frog wants to get to the other side of the road. The frog is currently
# located at position X and wants to get to a position greater than or equal to Y.
# The small frog always jumps a fixed distance, D.
#
# Count the minimal number of jumps that the small frog must perform to reach
# its target.
#
# Write a function:
#
# class Solution { public int solution(int X, int Y, int D); }
#
# that, given three integers X, Y and D, returns the minimal number of jumps
# from position X to a position equal to or greater than Y.
#
# For example, given:
#
#   X = 10
#   Y = 85
#   D = 30
# the function should return 3, because the frog will be positioned as follows:
#
# after the first jump, at position 10 + 30 = 40
# after the second jump, at position 10 + 30 + 30 = 70
# after the third jump, at position 10 + 30 + 30 + 30 = 100
# Write an efficient algorithm for the following assumptions:
#
# X, Y and D are integers within the range [1..1,000,000,000];
# X ≤ Y.
#
# ============== solution =================
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# known
#   - the frog starts at position X
#   - target is position greater than or equal to Y
#   - the frog jumps at a fixed distance D
#
# constraint
#   - X,Y,D are integers within the range [1 ... 1,000,000,000]

# goal: find the minimal number of jumps from position X to Y
#
#
# example
# Y = 50, X = 10, D = 30
#  answer -> 2
#   math.ceil((50 - 10) / 30)
#
# case
#   1. Y == 1
#   2. Y == D
#   3. Y > D
#
# Example
#   1. Y = 120
#
#
# pseudocode
#   1. return math.ceil((Y - X) / D)

import math

def solution(X, Y, D):
    # write your code in Python 3.6
    return math.ceil((Y - X) / D)
