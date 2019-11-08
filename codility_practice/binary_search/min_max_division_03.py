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
#================ solution ======================
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal:
#   - find the minimum value of largest sum given K and M
#
# known
#   - binary search algorithm should be used
#       - find the middle point
#       - check for solution
#       - if solution, return value
#           - travel until all possible ranges of values are expored via binary search
#       - if not solution, readjust min/max
#           - change min if k (current number of sublists) > K (target value of sublists) --> smaller value of k
#           - change max if k (current number of sublists) =< K (targest value of sublists) --> larger value of K
#               - here, also update the smallest_maximum
#
# constraint:
#   - N and K are integers within the range [1 ... 100,000]
#   - M is an integer within the range [0 ... 10,000]
#
# cases
#   1. K == 1 --> return sum(A)
#   2. 1 < K < N
#   3. K == N --> return max(A)
#
# brainstorming solution
#   1. initialize min, max
#   2. until min max crosses,
#   3. find the middle point
#   4. check for solution
#   5. if k > K, then readjust min (min = mid + 1)
#   6. if not 5, then readjust max (max = mid - 1) and update smallest_maximum
#
#   7. return the smallest maximum
def solution(K, M, A):
    #   1. initialize min, max
    A_min = max(A)
    A_max = sum(A)
    N = len(A)
    smallest_maximum = A_max

    if K == 1:
        return A_max

    if K == N:
        return A_min

    if N == 1:
        return A[0]

    #   2. until min max crosses
    while A_min <= A_max:

        #   3. find the middle point
        half_distance = (A_max - A_min) // 2
        mid = half_distance + A_min

        #   4. check for solution
        k, current_smallest_maximum = check(A, mid)

        #   5. if k > K, then readjust min (min = mid + 1)
        if k > K:
            A_min = mid + 1
        #   6. if not 5, then readjust max (max = mid - 1) and update smallest_maximum
        else:
            A_max = mid - 1
            smallest_maximum = min(smallest_maximum, current_smallest_maximum)

    #   7. return the smallest maximum
    return smallest_maximum

def check(A, mid):
    N = len(A)
    k = 1
    largest_sum = 0
    current_sum = A[0]

    for index in range(1, N):
        number = A[index]
        if current_sum + number > mid:
            k += 1
            largest_sum = max(current_sum, largest_sum)
            current_sum = number
        else:
            current_sum += number

    largest_sum = max(current_sum, largest_sum)

    return k, largest_sum