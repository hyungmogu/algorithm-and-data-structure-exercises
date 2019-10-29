# Equi Leader
#
#
# A non-empty array A consisting of N integers is given.

# The leader of this array is the value that occurs in more than half of the
# elements of A.

# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0],
# A[1], ..., A[S] and A[S + 1], A[S + 2], ...,
# A[N − 1] have leaders of the same value.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:

# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.

# Write a function:

# class Solution { public int solution(int[] A); }

# that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

# For example, given:

#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# the function should return 2, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].



# ============== Attempt # 1 (44%) ===================
#   - spent too much time being correct.
#   - didn't do too well on scale test

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


# input
#   - list of integers ()
#
# output
#   - integer (number of equi leaders)
#
#
# known
#   - leader = value that occurs more than half of elements (dominator)
#   - equi leader = leader on the left hand side (A[0], ... A[S]) and leader on the right hand side (A[S+1], ..., A[N-1]) have the same value

# constraints
#   1. N is an integer within the range [1 ... 100,000]

# cases
#   1. N == 1



# revised pseudocode
#   1. calculate leaders LHS
#   2. calculate leaders RHs


def solution(A):
    # write your code in Python 3.6
    N = len(A)

    edge_case_value = get_edge_case(A,N)

    if edge_case_value:
        return edge_case_value

    index = 0
    equi_leader_count = 0

    leaders_lhs = get_leaders_lhs(A,N)
    leaders_rhs = get_leaders_rhs(A,N)

    while index < N -1:

        if equi_leader_exists(N, index, leaders_lhs, leaders_rhs):
            equi_leader_count += 1

        index += 1

    return equi_leader_count

def get_edge_case(A,N):
    if N == 1:
        return 0

    return None

def get_leaders_lhs(A,N):
    numbers_frequency = {}
    leaders_list = [None] * N
    index = 0
    leader = None

    # 1. for element, index in A
    while index < N:
        # 2. add count to key 'element'
        number = A[index]
        n = A[:index+1]

        if number in numbers_frequency:
            numbers_frequency[number] += 1
        else:
            numbers_frequency[number] = 1

        # 3. set leader
        if leader is None:
            leader = number

        #   3.1 if current dominator has count more than len(A[:index+1]) // 2, set leader[index] = dominator
        if numbers_frequency[leader] > (len(n) // 2):
            leaders_list[index] = leader

        #   3,2 if A[index] has count more than len(A[:index+1]) // 2, set leader[index] = dominator and set dominator = element
        if numbers_frequency[number] > (len(n) // 2):
            leaders_list[index] = number
            leader = number

        index += 1

    return leaders_list

def get_leaders_rhs(A,N):
    numbers_frequency = {}
    leaders_list = [None] * N
    index = 0
    leader = None

    # 1. for element, index in A
    while index < N:
        index_reversed = (N-1) - index
        # 2. add count to key 'element'
        number = A[index_reversed]
        n = A[index_reversed:]

        if number in numbers_frequency:
            numbers_frequency[number] += 1
        else:
            numbers_frequency[number] = 1

        # 3. set leader
        if leader is None:
            leader = number

        #   3.1 if current dominator has count more than len(A[:index+1]) // 2, set leader[index] = dominator
        if numbers_frequency[leader] > (len(n) // 2):
            leaders_list[index] = leader

        #   3,2 if A[index] has count more than len(A[:index+1]) // 2, set leader[index] = dominator and set dominator = element
        if numbers_frequency[number] > (len(n) // 2):
            leaders_list[index] = number
            leader = number

        index += 1

    return leaders_list

def equi_leader_exists(N, index, leaders_lhs, leaders_rhs):
    if leaders_lhs[index] == leaders_rhs[(N - 2) - index]:
        return True
    return False



# ====================== Attempt # 2 (100%) ====================
#   What was done well
#       - usage of functions on major points --> less confusion && easier replacements when done wrong
#
#   Note
#       - shallow copy takes time
#       - cases cases cases

def solution(A):
    # write your code in Python 3.6
    N = len(A)

    edge_case_value = get_edge_case(A,N)

    if edge_case_value:
        return edge_case_value

    index = 0
    equi_leader_count = 0

    leaders_lhs = get_leaders_lhs(A,N)
    leaders_rhs = get_leaders_rhs(A,N)

    while index < N -1:

        if equi_leader_exists(N, index, leaders_lhs, leaders_rhs):
            equi_leader_count += 1

        index += 1

    return equi_leader_count

def get_edge_case(A,N):
    if N == 1:
        return 0

    return None

def get_leaders_lhs(A,N):
    numbers_frequency = {}
    leaders_list = [None] * N
    index = 0
    leader = None

    # 1. for element, index in A
    while index < N:
        # 2. add count to key 'element'
        number = A[index]
        n = index + 1

        if number in numbers_frequency:
            numbers_frequency[number] += 1
        else:
            numbers_frequency[number] = 1

        # 3. set leader
        if leader is None:
            leader = number

        #   3.1 if current dominator has count more than len(A[:index+1]) // 2, set leader[index] = dominator
        if numbers_frequency[leader] > (n // 2):
            leaders_list[index] = leader

        #   3,2 if A[index] has count more than len(A[:index+1]) // 2, set leader[index] = dominator and set dominator = element
        if numbers_frequency[number] > (n // 2):
            leaders_list[index] = number
            leader = number

        index += 1

    return leaders_list

def get_leaders_rhs(A,N):
    numbers_frequency = {}
    leaders_list = [None] * N
    index = 0
    leader = None

    # 1. for element, index in A
    while index < N:
        index_reversed = (N-1) - index
        # 2. add count to key 'element'
        number = A[index_reversed]
        n = index + 1

        if number in numbers_frequency:
            numbers_frequency[number] += 1
        else:
            numbers_frequency[number] = 1

        # 3. set leader
        if leader is None:
            leader = number

        #   3.1 if current dominator has count more than len(A[:index+1]) // 2, set leader[index] = dominator
        if numbers_frequency[leader] > (n // 2):
            leaders_list[index] = leader

        #   3,2 if A[index] has count more than len(A[:index+1]) // 2, set leader[index] = dominator and set dominator = element
        if numbers_frequency[number] > (n // 2):
            leaders_list[index] = number
            leader = number

        index += 1

    return leaders_list

def equi_leader_exists(N, index, leaders_lhs, leaders_rhs):
    if leaders_lhs[index] == None or leaders_rhs[(N - 2) - index] == None:
        return False

    if leaders_lhs[index] != leaders_rhs[(N - 2) - index]:
        return False
    return True