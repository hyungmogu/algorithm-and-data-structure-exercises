# Tie ropes
#
# ============= solution ==============

# greedy

def solution(K, A):
    # write your code in Python 3.6
    if K == 1:
        return len(A)

    index = 0
    maximal_rope_cnt = 0
    rope_length = 0

    N = len(A)
    A_sum = sum(A)

    if N == 1 and A[0] >= K:
        return 1

    if N == 1 and A[0] < K:
        return 0

    while index < len(A):
        rope_length += A[index]

        if rope_length >= K:
            maximal_rope_cnt += 1
            rope_length = 0

        index += 1


    return maximal_rope_cnt