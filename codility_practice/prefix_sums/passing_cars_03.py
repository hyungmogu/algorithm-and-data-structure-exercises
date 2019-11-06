# passing cars
# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
#
# A non-empty array A consisting of N integers is given. The consecutive elements of
# array A represent consecutive cars on a road.
#
# Array A contains only 0s and/or 1s:
#
# 0 represents a car traveling east,
# 1 represents a car traveling west.
# The goal is to count passing cars. We say that a pair of cars (P, Q), where
# 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling
# to the west.
#
# For example, consider array A such that:
#
#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
#
# Write a function:
#
# def solution(A)
#
# that, given a non-empty array A of N integers, returns the number of pairs of
# passing cars.
#
# The function should return −1 if the number of pairs of passing cars exceeds
# 1,000,000,000.
#
# For example, given:
#
#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# the function should return 5, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer that can have one of the following values: 0, 1.
#
#
# =============== solution ================
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal:
#   - find total number of pairs of passing cars
#
# constraint
#   - N is an integer within the range [1 ... 100,000]
#   - each element of array A is an integer that can have one of the following valeus: 0,1
#
# known
#   - car labeled '1' is traveling west
#   - car lebeled '0' is traveling east
#   - return -1 if pairs of passing cars exceeds 1,000,000,000
#
# cases
#   1. if len(A) == 1 --> return -1
#   2. if len(A) != 1
#
#
# pseudocode
#   1. count total number of 1s
#   2. for each number in A
#   3. if number is 0, add number of 1s to totals
#   4. if number is 1, decemrement number of 1s
#
#   5. return totals
def solution(A):
    number_of_1s = 0
    totals = 0
    LIMIT = 1000000000
    N = len(A)

    if N == 1:
        return 0

    #   1. count total number of 1s
    for number in A:
        if number == 1:
            number_of_1s += 1

    #   2. for each number in A
    for number in A:
        #   3. if number is 0, add number of 1s to totals
        if number == 0:
            totals += number_of_1s
        #   4. if number is 1, decemrement number of 1s
        else:
            number_of_1s -= 1

    if totals > LIMIT:
        return -1

    #   5. return totals
    return totals