# Max Product of Three
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

# =================== solution =======================

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# Input
#   - list of integers
#
# output
#   - integer (maximal product of three integers)
#
# constraint
#   - N is an integer in range [3 ... 100,000]
#   - each element in array is in range [-1000 ... 1000]
#
# cases
#   1. if there are more than 2 negative elements
#       - if A[-1] * A[-2] * A[0] > A[0] * A[1] * A[2], then return A[-1] * A[-2] * A[0]
#   2. if there is one negative element
#       - product of A[0], A[1], A[2]
#   3. if all positive elements exist
#       - product of A[0], A[1], A[2]

# pseudocode
#   1. sort elements in array (reversed)

#   2. return A[0] * A[1] * A[2]

def solution(A):
    A.sort(reverse=True)

    if (A[-1] * A[-2] * A[0]) > (A[0] * A[1] * A[2]):
        return A[-1] * A[-2] * A[0]

    return A[0] * A[1] * A[2]


if __name__ == '__main__':
    A_case_1 = [2,3,4,-5,6]

    expected_1 = 60

    solution_1 = solution(A_case_1)

    assert expected_1 == solution_1


