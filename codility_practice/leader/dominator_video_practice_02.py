# Dominator
# https://app.codility.com/programmers/lessons/8-leader/dominator/
#
# An array A consisting of N integers is given. The dominator of array A is the
# value that occurs in more than half of the elements of A.
#
#
# For example, consider array A such that
#
#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely
# in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.
#
# Write a function
#
# def solution(A)
#
# that, given an array A consisting of N integers, returns index of any element
# of array A in which the dominator of A occurs. The function should return −1
# if array A does not have a dominator.
#
# For example, given array A such that
#
#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# the function may return 0, 2, 4, 6 or 7, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

# ==================== solution ========================
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal:
#   - given an array of elements A, find index of element with more than half of A
#
# input
#   - list of integers A
#
# output
#   - integer (index of element containing more than half of elements in A)
#
# constraints
#   - N is in between [0 ... 100,000]
#
# known
#   - index of dominator can be anything as long as it is in array
#   - if dominator doesn't exist, then return -1
#
# cases
#   1. N == 0 --> return -1
#   2. N == 1 --> return 0
#   3. N > 1
#
# Example
#   [3,4,3,2,3,-1,3,3]
#   output --> 3
#
#   step 1: count
#   [3,4,3,2,3,-1,3,3] -> {key: [index, count]} {3: [0,5], 4: [1,1], 2: [3,1], -1: [5,1]} 'number_frequency'
#
#   step 2: walk over each key in number_frequency and if dominator exists, return index
#
#   step 3: return -1 if dominator doesn't exist
#
#   Dominator
#       odd?
#           [3,4,3,2,3,-1,3,3,3]
#
# brainstorming solution
def solution(A):
    N = len(A)
    dominator_threshold = N // 2
    number_frequency = {}

    if N == 0:
        return -1

    if N == 1:
        return 0

    #   1. count
    for index in range(N):
        number = A[index]
        if number in number_frequency:
            number_frequency[number][1] += 1
        else:
            number_frequency[number] = [index, 1]

    #   2. walk over each key in number_frequency and if dominator exists, return index
    for key in number_frequency:
        number_index = number_frequency[key][0]
        number_cnt = number_frequency[key][1]

        if number_cnt > dominator_threshold:
            return number_index

    #   3. return -1 if dominator doesn't exist
    return -1