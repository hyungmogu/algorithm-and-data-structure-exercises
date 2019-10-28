# Frog Jump
#
# A small frog wants to get to the other side of the road. The frog is currently
# located at position X and wants to get to a position greater than or equal to Y.
# The small frog always jumps a fixed distance, D.

# Count the minimal number of jumps that the small frog must perform to reach
# its target.

# Write a function:

# class Solution { public int solution(int X, int Y, int D); }

# that, given three integers X, Y and D, returns the minimal number of jumps
# from position X to a position equal to or greater than Y.

# For example, given:

#   X = 10
#   Y = 85
#   D = 30
# the function should return 3, because the frog will be positioned as follows:

# after the first jump, at position 10 + 30 = 40
# after the second jump, at position 10 + 30 + 30 = 70
# after the third jump, at position 10 + 30 + 30 + 30 = 100
# Write an efficient algorithm for the following assumptions:

# X, Y and D are integers within the range [1..1,000,000,000];
# X ≤ Y.
#
# =============== solution =================

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal: calculate the minimal number of jumps required for
# the frog to reach distance Y given that frog jumps a fixed distance D

# caess
#   1. when Y - X <= 0 --> return 0
#   2. when Y - X > 0 and Y - X <= D --> return 1
#   3. when Y - X > 0 and Y - X > D --> calculate

# pseudocode
#   1. subtract Y from from X
#   2. if Y - X <= 0, return 0
#   3. if Y - X <= D, return 1
#   4. return math.ceil((Y - X) % D)

#
# Has O(1) time complexity and O(1) spatial complexity

import math

def solution(X, Y, D):
    #   1. subtract Y from from X
    #   2. if Y - X <= 0, return 0
    if Y - X <= 0:
        return 0

    #   3. if Y - X <= D, return 1
    if Y - X <= D:
        return 1

    #   4. return math.ceil((Y - X) % D)
    return math.ceil((Y - X) / float(D))
