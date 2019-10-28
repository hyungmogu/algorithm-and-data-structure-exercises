# passing cars
#
# A non-empty array A consisting of N integers is given. The consecutive elements
# of array A represent consecutive cars on a road.
#
# Array A contains only 0s and/or 1s:
#
# 0 represents a car traveling east,
# 1 represents a car traveling west.
# The goal is to count passing cars. We say that a pair of cars (P, Q), where
# 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to
# the west.
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
# class Solution { public int solution(int[] A); }
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


# ======== solution ========


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# input
#   - list of integers
#
# output
#   - intger (total pairs of passing cars)
#
# known
#   - 0 represent car traveling east
#   - 1 represents car traveling west
#   -
#
# constraints
#   - if pair of passing cars exceeds 1,000,000,000, then return -1
#
#
# pattern
#   - total pairs of passing cars = sum of 1s in front of zeros
#       i.e. [0,1,0,1,1]
#           - 1st 0 --> 3 1s in front
#           - 2nd 0 --> 2 1s in front
#           - 3 + 2 = 5
# cases
#   1.if len(A) == 1 --> return 1
#   2. if len(A) != 1
#       2.1 if total crossings exceeds 1,000,000,000
#
# pseudocode
#   1. initialize index = 0, crossings_total, LIMIT = 1,000,000,00
#   2. get total of all 1s in A and store in cars_traveling_west
#   3. while index = 0, and is less than A
#   4. if crossings_total exceeds 1,000,000,000, then return -1
#   5. if A[index] == 0, add cars_traveling_west to crossings_total
#   6. if A[index] == 1, decrement cars_traveling_west
#   7. return crossings total
#
# time complexity O(N), and spatial complexity O(1)

def solution(A):
    if len(A) == 1:
        return 0

    #   1. initialize index = 0, crossings_total, LIMIT = 1,000,000,00
    index = crossings_total = index = 0
    LIMIT = 1000000000

    #   2. get total of all 1s in A and store in cars_traveling_west
    cars_traveling_west = sum(A)
    #   3. while index = 0, and is less than A
    while index < len(A):

        #   4. if crossings_total exceeds 1,000,000,000, then return -1
        if crossings_total > LIMIT:
            return -1
        #   5. if A[index] == 0, add cars_traveling_west to crossings_total
        if A[index] == 0:
            crossings_total += cars_traveling_west
        #   6. if A[index] == 1, decrement cars_traveling_west
        if A[index] == 1:
            cars_traveling_west -= 1

        index += 1
    #   7. return crossings total
    return crossings_total

    # time complexity O(N), and spatial complexity O(1)