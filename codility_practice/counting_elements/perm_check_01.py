# Perm Check
#
#A non-empty array A consisting of N integers is given.
#
# A permutation is a sequence containing each element from 1 to N once, and only once.
#
# For example, array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# is not a permutation, because value 2 is missing.
#
# The goal is to check whether array A is a permutation.
#
# Write a function:
#
# class Solution { public int solution(int[] A); }
#
# that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
#
# For example, given array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# the function should return 1.
#
# Given array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# the function should return 0.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].

# ================= Solution ============

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# input
#   -  List of integers
#
# output
#   - integer (1 if permutation and 0 if not)
#
# permutation
#   -
#
# constraints
#   -  A is has elements within the range [1 ... 100,000]
#   - every element in array A is an integer within the range
#   [1 ... 1,000,000,000]
#
# Known
#   - is a permutation if all 1 ... N is in the list
#   - is a permutation if A has element ONCE and ONLY ONCE
#
#
# cases
#   1. if N == 1 and A[0] !== 1 <-- return 0
#   2. if N == 1 and A[0] == 1 <-- return 1
#   3. if N != 1 <-- what we are calculating
#       3.1 repeating elements
#       3.2 non-repeating elements
#
# pseudocode
#   1. initialize 'requirements_set' with values 1 ... N
#   2. for element in A
#   3. if element in requirements_set remove element
#   4. if element not in requirements_set, return 0
#   5. after loop, if length of requirements_set != 0, then return 0
#   6. return 1
#
# Has time complexity of O(N) and spatial complexity of O(N)
#
#

def solution(A):
    # write your code in Python 3.6
    #   1. initialize 'requirements_set' with values 1 ... N
    N = len(A)
    requirements_set = set(range(1,N+1))
    #   2. for element in A
    for element in A:
        #   3. if element in requirements_set remove element
        if element not in requirements_set:
            return 0
        #   4. if element not in requirements_set, return 0
        else:
            requirements_set.remove(element)
    #   5. after loop, if length of requirements_set != 0, then return 0
    if len(requirements_set) != 0:
        return 0
    #   6. return 1
    return 1


if __name__ == '__main__':
    A_case_1 = [4,1,3,2]
    A_case_2 = [4,1,3]

    expected_1 = 1
    expected_2 = 0

    solution_1 = solution(A_case_1)
    solution_2 = solution(A_case_2)

    assert expected_1 == solution_1
    assert expected_2 == solution_2