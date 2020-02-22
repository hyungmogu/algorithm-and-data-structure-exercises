# number solitaire
#
# =============== solution ===================
#   - What to improve on
#       - the fine details (7 and 6)
#
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# 1. find dp of first 6 moves
# 2. find dp until index == N
# 3. return dp
def solution(A):
    index = 1
    N = len(A)
    dp = [A[0]] + [0] * (N-1)

    # 1. find dp of first 5 moves
    while index < min(7,N):
        dp[index] = A[index] + max(dp[:index])
        index += 1

    # 2. find dp until index == N
    while index < N:
        dp[index] = A[index] + max(dp[index-6:index])
        index += 1

    # 3. return dp
    return dp[-1]
