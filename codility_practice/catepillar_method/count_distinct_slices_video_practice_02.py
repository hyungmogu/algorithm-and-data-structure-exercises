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
#
# ================ solution =================
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal
#   - given an array of integers A, find total number of continuous and distinct slices
#
# input
#   - list of integers A
#   - integer M (the upperbound of value of elements in A)
#
# constraints
#   - N is an integer in between [0 ... 100,000]
#   - M is an integer in range [0 ... 100,000]
#
# known
#   - continus slice means in between two indexes, there are no repeating elements
#   - build algorithm using catepillar method
#
# example
# A = [3,4,5,5,2]
#
# output: 9
#
# [3,4,5,5,2]
#  0 1 2 3 4
#
# (0,0), (0,1), (0,2), (1,1), (1,2), (2,2), (3,3),(3,4),(4,4)
#
# slices = slices + ((front - back) + 1)
#
# Example (solving using catepillar method)
#   step 1: front: 0 and back: 0
# [3,4,5,5,2] -> 1 distinct slice --> (0,0)
#  f
#  b
#
#   step 2: front: 1 and back: 0
# [3,4,5,5,2] -> 3 distinct slices -> (0,0), (0,1), (1,1)
#    f
#  b
#
#   step 3: front: 2 and back: 0
# [3,4,5,5,2] -> 6 distinct slices --> (0,0), (0,1), (0,2), (1,1), (1,2), (2,2)
#      f
#  b
#
#
#   step 4: frontL 3 and back: 0
# [3,4,5,5,2] --> not distinct slice --> move b until slices become distinct
#        f
#  b
#
#   step 5: front: 3 and back: 3
# [3,4,5,5,2] --> 7 distinct slices -->
#        f
#        b
#
# cases
#   1. N == 1 --> return 1
#   2. N != 1
#   3. N != 1 and slices > 1,000,000,000 --> return 1,000,000,000
#
# brainstorming soluion
#   1. for each element in A
#   2. if not distinct, propate back until it becomes distinct
#   3. update slices count
#
#   4. if number of slices is greater than a billion, then return billion
#   5. return number of slices
#
# Time complexity is O(N) and spatial compelxity is O(1)
def solution(M, A):
    N = len(A)
    numbers_set = set()
    back = front = 0
    slices = 0

    LIMIT = 1000000000

    if N == 1:
        return 1

    #   1. for each element in A
    while front < N:
        number = A[front]
        #   2. if not distinct, propate back until it becomes distinct
        if number in numbers_set:
            numbers_set.remove(A[back])
            back += 1
            continue

        #   3. update slices count
        slices += (front-back) + 1
        numbers_set.add(number)
        front += 1

    #   4. if number of slices is greater than a billion, then return billion
    if slices > LIMIT:
        return LIMIT
    #   5. return number of slices    pass
    return slices