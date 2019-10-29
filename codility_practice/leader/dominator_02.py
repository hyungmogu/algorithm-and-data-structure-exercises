# Dominator
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


# =========== solution ===============

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# input
#   - list of Integers
#
# output
#   - integer (index of dominator)
#
# knwon
#   - dominator --> elements occuring more than half times
#
# constraints
#   1.N in range [0 ... 100,000 ]
#   2. each element of array A is an integer within the range [-MAXINT...MAXINT]
#
# cases
#   1. N == 0 --> return -1
#   2. N == 1 --> return 0
#   3. N != 1
#
# pseudocode
#   1. for each number and index in A
#   2. if number in number_frequency, raise count by 1, or if not, set its value to 1
#   3. if number_frequency[number] is dominator, then return index
#   4. if all fails, then return -1
#
# time frequency O(N) and spatial complexity of O(N)

def solution(A):
    N = len(A)
    index = 0
    number_frequency = {}

    if N == 0:
        return -1

    if N == 1:
        return 0

    #   1. for each number and index in A
    while index < N:
        number = A[index]
        #   2. if number in number_frequency, raise count by 1, or if not, set its value to 1
        if number in number_frequency:
            number_frequency[number] += 1
        else:
            number_frequency[number] = 1

        #   3. if number_frequency[number] is dominator, then return index
        if number_frequency[number] > (N // 2):
            return index

        index +=1
    #   4. if all fails, then return -1
    return -1
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# input
#   - list of Integers
#
# output
#   - integer (index of dominator)
#
# knwon
#   - dominator --> elements occuring more than half times
#
# constraints
#   1.N in range [0 ... 100,000 ]
#   2. each element of array A is an integer within the range [-MAXINT...MAXINT]
#
# cases
#   1. N == 0 --> return -1
#   2. N == 1 --> return 0
#   3. N != 1
#       3.1 when 1 dominator exists
#       3.2 when 2 dominators exists
#
# pseudocode
#   1. for each number and index in A
#   2. if number in number_frequency, raise count by 1, or if not, set its value to 1
#   3. if number_frequency[number] is dominator, then return index
#   4. if all fails, then return -1
#
# time frequency O(N) and spatial complexity of O(N)

def solution(A):
    N = len(A)
    index = 0
    number_frequency = {}

    if N == 0:
        return -1

    if N == 1:
        return 0

    #   1. for each number and index in A
    while index < N:
        number = A[index]
        #   2. if number in number_frequency, raise count by 1, or if not, set its value to 1
        if number in number_frequency:
            number_frequency[number] += 1
        else:
            number_frequency[number] = 1

        #   3. if number_frequency[number] is dominator, then return index
        if is_dominator(number_frequency[number], N):
            return index

        index +=1
    #   4. if all fails, then return -1
    return -1


def is_dominator(number_count, N):
    if number_count > (N // 2):
        return True

    return False


