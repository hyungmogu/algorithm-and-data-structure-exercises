# Count Triangles
#
#  ============= solution ==============
#   - One area of improvement
#       - establish brute force solution first
#           - spent too much time trying establish efficient solutions first time
#
#   - What I had done well
#       - using examples

def solution(A):
    # write your code in Python 3.6
    index_p = 0
    triangle_cnt = 0
    N = len(A)

    A.sort()

    for index_p in range(N):
        index_r = index_p + 2
        for index_q in range(index_p + 1, N):
            while index_r < N and is_triangle(A[index_p], A[index_q], A[index_r]):

                if is_triangle(A[index_p], A[index_q], A[index_r]):
                    index_r += 1

            triangle_cnt += index_r - index_q - 1
        index_p += 1

    return triangle_cnt

def is_triangle(A_p, A_q, A_r):

    if ((A_p + A_q > A_r) and
        (A_q + A_r > A_p) and
        (A_r + A_p > A_q)):

        return True

    return False