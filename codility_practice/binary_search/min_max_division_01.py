# Min Max Division
#
# You are given integers K, M and a non-empty array A consisting of N integers.
# Every element of the array is not greater than M.
#
# You should divide this array into K blocks of consecutive elements. The size
# of the block is any integer between 0 and N. Every element of the array should
# belong to some block.
#
# The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum
# of empty block equals 0.
#
# The large sum is the maximal sum of any block.
#
# For example, you are given integers K = 3, M = 5 and array A such that:
#
#   A[0] = 2
#   A[1] = 1
#   A[2] = 5
#   A[3] = 1
#   A[4] = 2
#   A[5] = 2
#   A[6] = 2
# The array can be divided, for example, into the following blocks:
#
# [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
# [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
# [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
# [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
# The goal is to minimize the large sum. In the above example, 6 is the minimal
# large sum.
#
# Write a function:
#
# def solution(K, M, A)
#
# that, given integers K, M and a non-empty array A consisting of N integers,
# returns the minimal large sum.
#
# For example, given K = 3, M = 5 and array A such that:
#
#   A[0] = 2
#   A[1] = 1
#   A[2] = 5
#   A[3] = 1
#   A[4] = 2
#   A[5] = 2
#   A[6] = 2
# the function should return 6, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N and K are integers within the range [1..100,000];
# M is an integer within the range [0..10,000];
# each element of array A is an integer within the range [0..M].

# ============================


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# input
#   - list of integers
# output
#   - integer
#
# constraints
#
# A = [2,1,5,1,2,2,2]
#
# pointers = [1,2,3,len(A)-2]
#
# pseudocode
#   1. put all pointers except last one after another
#   2. if the size of largest array is > M, then decrement last pointer until satisfied
#   3. find the current largest sum of elements, and store in large_sum
#   4. if large_sum > large_sum_max, return current value
#   5. if not solution move each pointer by len(nextArr) // 2 (pointer on lhs move to right, and pointer on right move to left)
#   6. if pointers cross, then move in opposite direction
