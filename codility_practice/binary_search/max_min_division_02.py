
# ========= attempt 1 ================


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# cases 1
#

# 1, get max as its minimum store in floor

# 2. get sum as its maximum store in ceiling
# 3. find the middle
# 4. check if solution has reached (floor and ceiling)
# 5. return value if solution exists

# cases
#

import sys

def solution(K, M, A):
    N = len(A)
    floor = max(A)
    ceiling = sum(A)
    edge_case_value = get_edge_case(A,N,M,floor,ceiling)

    if edge_case_value != None:
        return edge_case_value

    # 1, get max as its minimum store in floor
    # 2. get sum as its maximum store in ceiling

    largest_smallest = sys.maxsize

    while floor <= ceiling:
        # 3. find the middle
        half_distance = (ceiling - floor) // 2
        middle = half_distance + floor

        # 4. check if solution has reached (floor and ceiling)
        k, current_largest_smallest = check(A,middle)
        # 5. return value if solution exists
        if k < K:
            ceiling = middle - 1
            largest_smallest = min(largest_smallest, current_largest_smallest)
        else:
            floor = middle + 1


    return largest_smallest

def check(A, mid):
    k = 1
    N = len(A)
    index = 1
    largest_sum = 0
    slice_ending = A[0]

    while index < N:
        if slice_ending + A[index] > mid:
            k += 1
            largest_sum = max(slice_ending, largest_sum)
            slice_ending = A[index]
        else:
            slice_ending += A[index]

        index += 1

    largest_sum = max(slice_ending, largest_sum)

    return k, largest_sum

def get_edge_case(A,N,M,floor,ceiling):
    if N == 1:
        return A[0]

    if M == len(A):
        return floor

    if M == 1:
        return ceiling

    return None


# ========= attempt 2 ================

# Solution checking. Couldn't find errors.
