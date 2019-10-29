# Max Profit
# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/

# ======================= solution ============================

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# input
#   - list of integers
#
# output
#   - integer (maximum profit by buying on a day and selling on the other day)
#
# known
#   - shares can be bought and sold on the same day
#
# constraints
#   - size of list N in between [0 ... 400,000]
#   - element of array A in between [0 ... 200,000]
#
#
#
# cases (Major)
#   1. N == 0 --> return 0
#   2. N == 1 --> return 0
#   3. N > 1
#       - > return 0 if it is impossible to gain any profit
#
# pseudocode
#   1. find profit margin of buying and selling on the next day store this in diff
#   2. for each value in diff
#   3. get profit_ending
#   4. get max_profit
#   5. at the end of loop, return max_profit
#
def solution(A):
    #   1. find profit margin of buying and selling on the next day store this in diff
    N = len(A)

    edge_case_value = get_edge_case(A, N)

    if edge_case_value:
        return edge_case_value

    index = 0
    diff = get_diff(A, N)
    profit_ending = max_profit = 0

    #   2. for each value in diff
    while index < len(diff):
        #   3. get profit_ending
        profit_ending = max(0, profit_ending + diff[index])
        #   4. get max_profit
        max_profit = max(profit_ending, max_profit)

        index += 1

    #   5. at the end of loop, return max_profit
    return max_profit

def get_diff(A, N):
    index = 1
    diff = []

    while index < N:
        diff.append(A[index] - A[index-1])
        index += 1

    return diff

def get_edge_case(A, N):

    if N == 0 or N == 1:
        return 0

    return None