# Permutation Check
# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
#
#A non-empty array A consisting of N integers is given.
#
# A permutation is a sequence containing each element from 1 to N once, and only once.
#
# For example, array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# is not a permutation, because value 2 is missing.
#
# The goal is to check whether array A is a permutation.
#
# Write a function:
#
# class Solution { public int solution(int[] A); }
#
# that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
#
# For example, given array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# the function should return 1.
#
# Given array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# the function should return 0.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].

#
# ================ solution ===================
#
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal:
#   - check whether array A is a permutation
#
# constraint
#   - N is an integer witin the range [1 ... 100,000]
#   - each element of array A is an integer in range [1 ... 1,000,000,000]
#
# knwon
#   - if not permutation, return 0
#   - if poermutation, return 1
#
# cases
#   1. A == 1 --> return 1
#   2. A != 1
#
# pseudocode
#   1. turn A into a set
#   2. if an element is missing, return 0
#   3. if not missing, check for duplicates
#   4. if all is well, return 1

#
# time complexity O(N), spatial complexity O(N)

def solution(A):
    if len(A) == 1 and A[0] != 1:
        return 0

    if len(A) == 1 and A[0] == 1:
        return 1

    #   1. turn A into a set
    N = len(A)
    A_set = set(A)

    #   2. if an element is missing, return 0
    for number in range (1, N+1):
        if not number in A_set:
            return 0

    #   3. if not missing, check for duplicates
    for number in A:
        if not number in A_set:
            return 0
        else:
            A_set.remove(number)

    #   4. if all is well, return 1
    return 1