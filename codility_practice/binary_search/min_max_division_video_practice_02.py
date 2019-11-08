# min max division
# https://app.codility.com/programmers/lessons/14-binary_search_algorithm/min_max_division/
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
#
#
# =============== solution ====================
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal
#   - given the value of K, and A, find the minimal large sum
#
# input
#   - K (integer, threshold limit of number of sublists)
#   - M (integer, threshold limit of VALUE of element in A)
#   - A (list of integers)
#
# output
#   - integer (smallest large sum)
#
# constraints
#   - N and K are in range [1 ... 100,000]
#   - M is in between [0 ... 10,0000]
#
# knowns
#   1. M can be safely ignored in the design of this algorithm
#   2. use binary search to find the smallest large sum
#       - until the stopping condition
#       - find the middle point
#       - check the solution at middle point
#       - return value if solution
#       - otherwise, adjust lower bound and upper bound
#
# cases
#   1. K == 1 --> sum(A)
#   2. 1 < K < N --> covered in algorithm
#   3. K == N --> max(A)
#   4. N == 1 --> A[0]
#
# brainstorming solution
def solution(K, M, A):
    N = len(A)
    #   1. lower bound --> min --> smallest possible large sum a problem can have --> max(A)
    A_min = max(A)
    #   2. upper bound --> max --> largest possible large sum a problem can have --> sum(A)
    A_max = sum(A)
    minimal_largest_sum = A_max

    if K == 1:
        return A_max

    if K == N:
        return A_min

    if N == 1:
        return A[0]

    #   - until the stopping condition
    while A_min <= A_max:
        #   - find the middle point
        half_distance = (A_max - A_min) // 2
        mid = half_distance + A_min

        #   - check the solution at middle point
        k, current_minimal_largest_sum = check(A, mid)

        #   - otherwise, adjust lower bound and upper bound
        if k > K:
            A_min = mid + 1
        else:
            A_max = mid - 1
            minimal_largest_sum = min(current_minimal_largest_sum, minimal_largest_sum)

    return minimal_largest_sum


def check(A, mid):
    k = 1
    N = len(A)
    largest_sum = 0
    current_sum = A[0]

    for index in range(1,N):
        number = A[index]

        if current_sum + number > mid:
            k += 1
            largest_sum = max(current_sum, largest_sum)
            current_sum = number
        else:
            current_sum += number

    largest_sum = max(current_sum, largest_sum)

    return k, largest_sum
