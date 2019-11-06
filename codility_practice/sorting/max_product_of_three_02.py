# Max Product of Three
# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
#
#
# A non-empty array A consisting of N integers is given. The product of triplet
# (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
#
# For example, array A such that:
#
#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# contains the following example triplets:
#
# (0, 1, 2), product is −3 * 1 * 2 = −6
# (1, 2, 4), product is 1 * 2 * 5 = 10
# (2, 4, 5), product is 2 * 5 * 6 = 60
# Your goal is to find the maximal product of any triplet.
#
# Write a function:
#
# def solution(A)
#
# that, given a non-empty array A, returns the value of the maximal product of any triplet.
#
# For example, given array A such that:
#
#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# the function should return 60, as the product of triplet (2, 4, 5) is maximal.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [−1,000..1,000]

#
# ==================== solution ========================
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal:
#   find three numbers where product is maximal
#
# known
#   - product of two negative # is positive
#   - product of two positive # is positive
#
# constraint
#   - N is an integer within the range [3 ... 100,000]
#   - each element of array A is an integer within the range [-1,000 ... 1,000]
#
#
# cases
#   1. N == 3
#   2. N != 3
#
# pseudocode
#   1. order elements in decreasing order
#   2. get product of a[0], a[1], a[2] and a[0], a[-1] and a[-2]
#   3. if product of a[0], a[1] and a[2] > a[0], a[-1], a[-2], then return product of a[0], a[1], a[2]

#   4. return value

def solution(A):
    #   1. order elements in decreasing order
    A.sort(reverse=True)
    product = 0

    #   2. get product of a[0], a[1], a[2] and a[0], a[-1] and a[-2]
    product_1 = A[0] * A[1] * A[2]
    product_2 = A[0] * A[-1] * A[-2]

    #   3. if product of a[0], a[1] and a[2] > a[0], a[-1], a[-2], then return product of a[0], a[1], a[2]
    if product_1 > product_2:
        return product_1

    #   4. return value
    return product_2
