# Cyclic Rotation
#
# An array A consisting of N integers is given. Rotation of the array means that
# each element is shifted right by one index, and the last element of the array
# is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6]
# is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).
#
# The goal is to rotate array A K times; that is, each element of A will be
# shifted to the right K times.
#
# Write a function:
#
# def solution(A, K)
#
# that, given an array A consisting of N integers and an integer K, returns
# the array A rotated K times.
#
# For example, given
#
#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:
#
#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given
#
#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0]
#
# Given
#
#     A = [1, 2, 3, 4]
#     K = 4
# the function should return [1, 2, 3, 4]
#
# Assume that:
#
# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].
# In your solution, focus on correctness. The performance of your solution will
# not be the focus of the assessment.
#
# =========== solution ===============

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
#    x                          x
# [3,8,9,7,6] --> hold 8 --> [3,3,9,7,6]
#      x
# [3,3,9,7,6] --> hold 9, release 8 --> [3,3,8,7,6]
#        x
# [3,3,8,7,6] --> hold 7, release 9 --> [3,3,8,9,6]
#          x
# [3,3,8,9,6] --> hold 6, release 7 --> [3,3,8,9,7]
#  x
# [3,3,8,9,6] --> release 6 --> [6,3,8,9,7] and repeat.
#
# current time complexity O(N^2) with spatial complexity O(1)
#
# ============
#
# better solution ? reduce time complexity to O(N) by setting time complexity to O(N)

def solution(A, K):
    # write your code in Python 3.6
    output = [None] * len(A)

    for index, value in enumerate(A):
        new_position = (index + K) % len(A)
        output[new_position] = value
    return output