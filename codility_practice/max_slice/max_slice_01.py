# Max Slice
# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/

# =============== Attempt # 1 (82%)  ================


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
#
# pseudocode
#   1. initialize slice_ending, max_sum, and smallest_negative to have value None,
# and index = 0, and N = len(A)
#   2. while index < N:
#   3. if should be a part of slice,
#       3.1. update slice_ending
#       3.2. update max_sum
#
#   4. if all negative numbers,
#       3.2 return smallest negative number
#
#   5. return max_sum

def solution(A):
    #   1. initialize slice_ending, max_sum, and smallest_negative to have value
    # None, and index = 0, and N = len(A)
    index = 0
    N = len(A)
    max_sum = None
    slice_ending = None
    smallest_negative = None

    edge_case_value = get_edge_case(A,N)

    if edge_case_value:
        return edge_case_value

    #   2. while index < N:
    while index < N:
        #   3. if should be a part of slice,
        if A[index] < 0:
            smallest_negative = (A[index] if ((smallest_negative == None) or
                                (smallest_negative > A[index])) else     smallest_negative)

        if is_a_part_of_slice(A, slice_ending, index):
            #       3.1. update slice_ending
            slice_ending = (A[index] if (slice_ending == None)
                            else (slice_ending + A[index]))

            #       3.2. update max_sum
            max_sum = (slice_ending if (max_sum == None)
                        else max(slice_ending, max_sum))
        else:
            slice_ending = None

        index += 1
    #   5. return max_sum
    if max_sum == None:
        return smallest_negative

    return max_sum

def is_a_part_of_slice(A, slice_ending, index):
    if slice_ending == None and A[index] > 0:
        return True

    if slice_ending != None and A[index] + slice_ending > 0:
        return True

    return False

def get_edge_case(A, N):
    if N == 1:
        return A[0]

    return None


# ===================== solution ==========================
#   - 0 returns as false


def solution(A):
    #   1. initialize slice_ending, max_sum, and smallest_negative to have value
    # None, and index = 0, and N = len(A)
    index = 0
    N = len(A)
    max_sum = None
    slice_ending = None
    smallest_negative = None

    edge_case_value = get_edge_case(A,N)

    if edge_case_value != None:
        return edge_case_value

    #   2. while index < N:
    while index < N:
        #   3. if should be a part of slice,
        if A[index] < 0:
            smallest_negative = (A[index] if ((smallest_negative == None) or
                                (smallest_negative < A[index])) else smallest_negative)

        if is_a_part_of_slice(A, slice_ending, index):
            #       3.1. update slice_ending
            slice_ending = (A[index] if (slice_ending == None)
                            else (slice_ending + A[index]))

            #       3.2. update max_sum
            max_sum = (slice_ending if (max_sum == None)
                        else max(slice_ending, max_sum))
        else:
            slice_ending = None

        index += 1
    #   5. return max_sum
    if max_sum == None:
        return smallest_negative

    return max_sum

def is_a_part_of_slice(A, slice_ending, index):
    if slice_ending == None and A[index] > 0:
        return True

    if slice_ending != None and A[index] + slice_ending > 0:
        return True

    return False

def get_edge_case(A, N):
    if N == 0:
        return 0

    if N == 1:
        return A[0]

    return None

