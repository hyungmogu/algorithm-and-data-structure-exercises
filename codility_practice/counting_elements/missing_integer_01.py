# Missing Integer
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer
# (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# ======== Attempt #1 (77%) ==========
# Need to be a little more careful with definitions and cases

def solution(A):
    # 1. for each element in array
    index = 1
    N = len(A)
    output = None

    A.sort()

    if N == 1 and A[0] >= 2:
        return 1
    elif N == 1 and A[0] == 1:
        return 2
    elif N == 1 and A[0] < 1:
        return 1

    while index < N:
        # 2. if gap exists, get the smallest positive number
        if gap_exists(A,index) and A[index] > 2:
            # 3. return the smallest positive numbe
            output = get_smallest_positive_number(A, index)
            return output
        index +=1

    if A[-1] < 0 or A[-1] == 0:
        return 1

    return A[-1] + 1

def gap_exists(A, index):
    if A[index] - A[index - 1] > 1:
        return True

    return False

def get_smallest_positive_number(A, index):
    if A[index-1] < 0:
        return 1

    return A[index-1] + 1
