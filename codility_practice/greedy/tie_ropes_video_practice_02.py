# Tie Ropes
# https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/
#
# There are N ropes numbered from 0 to N − 1, whose lengths are given in an
# array A, lying on the floor in a line. For each I (0 ≤ I < N), the length of
# rope I on the line is A[I].
#
# We say that two ropes I and I + 1 are adjacent. Two adjacent ropes can be tied
# together with a knot, and the length of the tied rope is the sum of lengths of
# both ropes. The resulting new rope can then be tied again.
#
# For a given integer K, the goal is to tie the ropes in such a way that the
# number of ropes whose length is greater than or equal to K is maximal.
#
# For example, consider K = 4 and array A such that:
#
#     A[0] = 1
#     A[1] = 2
#     A[2] = 3
#     A[3] = 4
#     A[4] = 1
#     A[5] = 1
#     A[6] = 3
# The ropes are shown in the figure below.
#
#
#
# We can tie:
#
# rope 1 with rope 2 to produce a rope of length A[1] + A[2] = 5;
# rope 4 with rope 5 with rope 6 to produce a rope of length A[4] + A[5] + A[6] = 5.
# After that, there will be three ropes whose lengths are greater than or equal
# to K = 4. It is not possible to produce four such ropes.
#
# Write a function:
#
# def solution(K, A)
#
# that, given an integer K and a non-empty array A of N integers, returns the
# maximum number of ropes of length greater than or equal to K that can be
# created.
#
# For example, given K = 4 and array A such that:
#
#     A[0] = 1
#     A[1] = 2
#     A[2] = 3
#     A[3] = 4
#     A[4] = 1
#     A[5] = 1
#     A[6] = 3
# the function should return 3, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# K is an integer within the range [1..1,000,000,000];
# each element of array A is an integer within the range [1..1,000,000,000].
#

# ============= solution ==============
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# Goal
#   - given a list of integers A and integer K, return integer representing maximum number of ropes
#     that's greater than or equal to K
#
# Input
#   - integer K
#   - list of integers A
#
# Ouput
#   - integer (total number of ropes greater than or equal to K)
#
# constraints
#   - N is an integer in between [1 ... 100,000]
#   - K is an integer in range [1 ... 1,000,000,000,000]
#   - value in array is in bettwen [1 ... 1,000,000,000,000]
#
# Knwon
#   - Only Adjacent ropes can be combined
#   - each rope must be greater than or equal to K
#   - solve this problem using greedy algorithm
#
# Example
#
# A = [1,2,3,4,1,1,3], K = 4
#
# output: 3
#
# rope # 1: {1,2,3}
# rope # 2: {4}
# rope # 3: {1,1,3}
#
# greedy algorithm has a peculiar characteristic --> One time pass
#
#
#
# brute force algorithm
#   1. trying all different cominbations and find the maximal number of ropes satisfying the criteria
#
#   TIme Complexity O(N^N), spatial complexity O(1)
#
# cases
#   1. if K == 1
#   2. if N == 1 and A[0] < K
#   3. if N == 1 and A[0] >= K
#   4. if N != 1 and A[0] < K
#   5. if N != 1 and A[0] >= K
#
# Imrpvoed solution (greedy algorithm)
#   1. while index < N, with index starting at 1,
#   2. if rope_sum + A[index] < K, rope_sum += A[index]
#   3. if rope_sum + A[index] >= K, increment rope_cnt, and set rope_sum = 0
#
#   4. return rope_cnt
#
#   Time complexity of O(N) and spatial complexity of O(1)
#
def solution(K, A):
    index = 1
    N = len(A)
    rope_sum = A[0]
    rope_cnt = 0

    if K == 1:
        return N

    if A[0] >= K:
        rope_cnt += 1
        rope_sum = 0

    #   1. while index < N, with index starting at 1,
    while index < N:
        #   2. if rope_sum + A[index] < K, rope_sum += A[index]
        if rope_sum + A[index] < K:
            rope_sum += A[index]

        #   3. if rope_sum + A[index] >= K, increment rope_cnt, and set rope_sum = 0
        else:
            rope_cnt += 1
            rope_sum = 0
        index += 1

    #   4. return rope_cnt
    return rope_cnt