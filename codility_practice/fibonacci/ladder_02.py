# Ladder
#
#https://app.codility.com/programmers/lessons/13-fibonacci_numbers/ladder/

# ============= attempt #1 (87 %) ====================
#   - time out error.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# use dynamic programming to achieve this case
#   1. base case
#       - N = 0
#           - 1 step
#       - N = 1
#           - 1 step
#       - N = 2
#           - 2 steps
#       - N = 3
#           - 3 steps
#       - N = 4
#           - 5 steps

# cases

# pseudocdoe
#   1. initialize dynamic programming, index, sequence
#   2. get values of dynamic programming for L many values
#   3. while index < N
#       3.1 get value of dp[N] where N = A[index]
#       3.2 set sequence[index] = dp[N] % (2 ** B[index])
#   4. return sequence
#
# has time complexity of O(max(N,L)) and spatial complexity of O(L)


def solution(A, B):
    #   1. initialize dynamic programming, index, sequence
    L = len(A)

    index = 0
    sequence = [0] * L

    #   2. get values of dynamic programming for L many values
    dp = get_dp(L)

    #   3. while index < N
    while index < L:
        N = A[index]
        #   4. get value of dp[N] where N = A[index]
        #   5. set sequence[index] = dp[N] % (2 ** B[index])
        sequence[index] = dp[N] % (2 ** B[index])
        index += 1

    #   4. return sequence
    return sequence

    # has time complexity of O(max(N,L)) and spatial complexity of O(L)


def get_dp(L):
    index = 1
    dp = [1] + [0] * L

    while index < L + 1:

        if index == 1:
            dp[index] = 1
            index += 1
            continue

        dp[index] = dp[index - 1] + dp[index - 2]

        index += 1

    return dp

