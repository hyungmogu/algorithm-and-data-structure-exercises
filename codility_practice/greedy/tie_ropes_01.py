# Tie Ropes
# https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/
#
# There are N ropes numbered from 0 to N − 1, whose lengths are given in an
# array A, lying on the floor in a line. For each I (0 ≤ I < N), the length of
# rope I on the line is A[I].
#
# We say that two ropes I and I + 1 are adjacent. Two adjacent ropes can be tied
# together with a knot, and the length of the tied rope is the sum of lengths of
# both ropes. The resulting new rope can then be tied again.
#
# For a given integer K, the goal is to tie the ropes in such a way that the
# number of ropes whose length is greater than or equal to K is maximal.
#
# For example, consider K = 4 and array A such that:
#
#     A[0] = 1
#     A[1] = 2
#     A[2] = 3
#     A[3] = 4
#     A[4] = 1
#     A[5] = 1
#     A[6] = 3
# The ropes are shown in the figure below.
#
#
#
# We can tie:
#
# rope 1 with rope 2 to produce a rope of length A[1] + A[2] = 5;
# rope 4 with rope 5 with rope 6 to produce a rope of length A[4] + A[5] + A[6] = 5.
# After that, there will be three ropes whose lengths are greater than or equal
# to K = 4. It is not possible to produce four such ropes.
#
# Write a function:
#
# def solution(K, A)
#
# that, given an integer K and a non-empty array A of N integers, returns the
# maximum number of ropes of length greater than or equal to K that can be
# created.
#
# For example, given K = 4 and array A such that:
#
#     A[0] = 1
#     A[1] = 2
#     A[2] = 3
#     A[3] = 4
#     A[4] = 1
#     A[5] = 1
#     A[6] = 3
# the function should return 3, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# K is an integer within the range [1..1,000,000,000];
# each element of array A is an integer within the range [1..1,000,000,000].
#
#
# =========== Solution ============
#
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# Time complexity O(N) spatial complexity O(1)
#
class Solution:
    def solve(self, K, A):
        if K == 1:
            return len(A)

        #   1. initialize index = 0, rope_length = 0, count = 0, index_last_rope = 0
        index = rope_length = count = 0

        #   2. while index < len(A):
        while index < len(A):
            #   3. if index - 1 == last_rope_index:
            #   4. otherwise
            #       3.2 sum A[index] and A[index-1] and store in 'rope_length '
            rope_length += A[index]
            #   5. if rope_length >= K,
            if rope_length >= K:
                #       5.1 increase count by 1
                count += 1
                #       5.2 reset rope length to 0
                rope_length = 0

            index +=1

        #   6. at the end of loop, return count
        return count


if __name__ == '__main__':
    A_case_1 = [1,2,3,4,1,1,3]
    K_case_1 = 4

    expected_1 = 3

    solution_1 = Solution().solve(K_case_1, A_case_1)

    assert expected_1 == solution_1
