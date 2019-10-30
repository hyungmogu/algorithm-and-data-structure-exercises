# Missing Integer
#
# ============= solution ==============
#   Area of improvement
#       - Case considerations. Base is fine, but doesn't do too well with edge cases

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    A.sort()

    if N == 1 and A[0] <= 0:
        return 1

    if N == 1 and A[0] == 1:
        return 2

    if N == 1 and A[0] >= 2:
        return 1

    if A[0] >= 2:
        return 1

    for index in range(1,N):
        if gap_exists(A, index) and A[index] >= 2:
            return get_smallest_positive_value(A, index)

    if A[-1] <= 0:
        return 1

    return A[-1] + 1

def gap_exists(A, index):
    if A[index] - A[index-1] > 1:
        return True
    return False

def get_smallest_positive_value(A, index):
    smallest_positive = 0

    if A[index - 1] <= 0:
        smallest_positive = 1

    if index - 1 == 0 and A[index -1] == 1:
        smallest_positive = 2

    if index - 1 == 0 and A[index - 1] >= 2:
        smallest_positive = 1

    if index - 1 > 0 and A[index - 1] >= 2:
        smallest_positive = A[index - 1] + 1

    return smallest_positive