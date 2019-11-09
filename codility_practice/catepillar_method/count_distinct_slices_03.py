# Count Distinct Slices
# https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/
#
#
# An integer M and a non-empty array A consisting of N non-negative integers are
# given. All integers in array A are less than or equal to M.
#
# A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array
# A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct
# slice is a slice consisting of only unique numbers. That is, no individual number
# occurs more than once in the slice.
#
# For example, consider integer M = 6 and array A such that:
#
#     A[0] = 3
#     A[1] = 4
#     A[2] = 5
#     A[3] = 5
#     A[4] = 2
# There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1),
# (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).
#
# The goal is to calculate the number of distinct slices.
#
# Write a function:
#
# def solution(M, A)
#
# that, given an integer M and a non-empty array A consisting of N integers,
# returns the number of distinct slices.
#
# If the number of distinct slices is greater than 1,000,000,000, the function
# should return 1,000,000,000.
#
# For example, given integer M = 6 and array A such that:
#
#     A[0] = 3
#     A[1] = 4
#     A[2] = 5
#     A[3] = 5
#     A[4] = 2
# the function should return 9, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# M is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..M].
#
# ============= Attempt ================
# Example returns 13, not 9.
#
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal
#   - find the toal number of continuous and distinct slices of A
#
# constraints
#   - N is an integer in range [1 ... 100,000]
#   - M is an integer in range [0 ... 100,000]
#
# known
#   - if # of distinct slices is greater than 1,000,000,000, then return 1,000,000,000
#   - Number of distinct slices between front and back = (front - back) + 1
#
# cases
#   1. N == 1
#
# pseudocode
def solution(M, A):
    N = len(A)
    numbers_set = set()
    LIMIT = 1000000000
    slices = 0

    back = 0
    front = 0

    if N == 1:
        return 1

    #   1. for each element in A, travel until repeating element found
    while front < N:
        number = A[front]
        # backward
        #   3. if back element found, move back until no repeatin gelement found
        if number in numbers_set:
            numbers_set.remove(number)
            back += 1

        # forward
        #   2. and for each element in A, update total number of slices
        numbers_set.add(number)
        slices += (front - back) + 1
        front += 1

    if slices > LIMIT:
        return LIMIT

    #   4. return total number of distinct slices
    return slices


# =============== solution ======================

# pseudocode
def solution(M, A):
    N = len(A)
    numbers_set = set()
    LIMIT = 1000000000
    slices = 0

    back = 0
    front = 0

    if N == 1:
        return 1

    #   1. for each element in A, travel until repeating element found
    while front < N:
        number = A[front]
        # backward
        #   3. if back element found, move back until no repeatin gelement found
        if number in numbers_set:
            number_back = A[back]
            numbers_set.remove(number_back)
            back += 1
            continue

        # forward
        #   2. and for each element in A, update total number of slices
        numbers_set.add(number)
        slices += (front - back) + 1
        front += 1

    if slices > LIMIT:
        return LIMIT

    #   4. return total number of distinct slices
    return slices
