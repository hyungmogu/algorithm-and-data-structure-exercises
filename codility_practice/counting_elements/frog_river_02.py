# Frog River
#
# A small frog wants to get to the other side of a river. The frog is initially
# located on one bank of the river (position 0) and wants to get to the opposite
# bank (position X+1). Leaves fall from a tree onto the surface of the river.

# You are given an array A consisting of N integers representing the falling
# leaves. A[K] represents the position where one leaf falls at time K, measured
# in seconds.

# The goal is to find the earliest time when the frog can jump to the other side
# of the river. The frog can cross only when leaves appear at every position across
# the river from 1 to X (that is, we want to find the earliest moment when all
# the positions from 1 to X are covered by leaves). You may assume that the speed
# of the current in the river is negligibly small, i.e. the leaves do not change
# their positions once they fall in the river.

# For example, you are given integer X = 5 and array A such that:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# In second 6, a leaf falls into position 5. This is the earliest time when leaves
# appear in every position across the river.

# Write a function:

# class Solution { public int solution(int X, int[] A); }

# that, given a non-empty array A consisting of N integers and integer X, returns
# the earliest time when the frog can jump to the other side of the river.

# If the frog is never able to jump to the other side of the river, the function
# should return −1.

# For example, given X = 5 and array A such that:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# the function should return 6, as explained above.

# Write an efficient algorithm for the following assumptions:

# N and X are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..X].


# ========== solution ==================

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# conditions
#   - return -1 if position not found / cannot cross the river

# brainstorming solution
def solution(X, A):
    #   1. put all elements in a set
    N = len(A)
    positions_set = set(range(1,X+1))
    index = 0

    #   2. for each element and index in array
    while index < N:
        #   3. if element is in set, remove
        if A[index] in positions_set:
            positions_set.remove(A[index])
        #   4. if length == 0, return index

        if len(positions_set) == 0:
            return index
        index += 1
    return -1

# time complexity O(N), spatial complexity O(10

if __name__ == '__main__':
    A_case_1 = [1,3,1,4,2,3,5,4]
    X_case_1 = 5

    A_case_2 = []
    X_case_2 = -1

    A_case_3 = [1,3,1,4,2,3,5,4]
    X_case_3 = 10

    expected_1 = 6
    expected_2 = -1
    expected_3 = -1

    solution_1 = solution(A_case_1, X_case_1)
    solution_2 = solution(A_case_2, X_case_2)
    solution_3 = solution(A_case_3, X_case_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
