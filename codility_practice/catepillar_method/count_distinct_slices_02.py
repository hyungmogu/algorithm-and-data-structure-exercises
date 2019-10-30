# distinct slices
# ============ solution ===========
#   - mistake
#       - Not considered enough test cases.
#       - should have thought a little more out of box
#
#   - What I had done well
#       - building solution step by step
#
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # write your code in Python 3.6
    front = back = 0
    N = len(A)
    total_slices = 0
    slices = 0
    elements_set = set()

    LIMIT = 1000000000

    if N == 1:
        return 1

    while front < N:
        #2. check if A[index] is a repeat
        if A[front] in elements_set:
            # reinitialize
            elements_set.remove(A[back])
            back += 1
            continue

        if slices > LIMIT:
            return LIMIT

        slices = slices + ((front - back) + 1)
        elements_set.add(A[front])

        front += 1

    total_slices += slices

    return total_slices
