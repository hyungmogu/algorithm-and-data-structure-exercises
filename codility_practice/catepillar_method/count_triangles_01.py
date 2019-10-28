# Count Triangles
#
# An array A consisting of N integers is given. A triplet (P, Q, R) is triangular
# if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R].
# In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

# A[P] + A[Q] > A[R],
# A[Q] + A[R] > A[P],
# A[R] + A[P] > A[Q].
# For example, consider array A such that:

#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 12
# There are four triangular triplets that can be constructed from elements of this
# array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

# Write a function:

# def solution(A)

# that, given an array A consisting of N integers, returns the number of triangular
# triplets in this array.

# For example, given array A such that:

#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 12
# the function should return 4, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..1,000];
# each element of array A is an integer within the range [1..1,000,000,000].


# ================== solution =======================

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# input
#   - list of integers
# output
#   -integers
#
# constraint
#   - N integer in range [0 ... 1,000]
#   - element in A in between [1 ... 1,000,000,000]
#
# cases
#   1. len(A) == 0 || len(A) == 1 || len(A) == 2 --> 0
#   2. len(A) != 2

# brainstorming solution
class Solution:
    def solve(self, A):
        if len(A) < 3:
            return 0

        #   1. initialize back, front, num_triangles
        back = total_num_triangles = 0
        front = 2

        #   2. sort the array
        A.sort()

        #   3. starting at front == 2,
        while front < len(A):
            #       2.1 if [back:front+1] has a triangle / triangles, raise num_count by 1
            total_num_triangles += self.count_triangles(A[back:front + 1])
            #   4. if size of [back:front+1] is 3, move front by 1
            if len(A[back:front+1]) == 3:
                front += 1
                continue

            #   5. if size of [back:front+1] is 4, move back by 1
            back += 1

        #   6. repeat the process until front is the size of Array
        return total_num_triangles

    def count_triangles(self, points):
        count = 0
        if len(points) == 3 and self.is_triangle(points[0], points[1], points[2]):
            count += 1

        if len(points) == 4 and self.is_triangle(points[0], points[1], points[3]):
            count += 1

        if len(points) == 4 and self.is_triangle(points[0], points[2], points[3]):
            count += 1

        return count

    def is_triangle(self, A_p, A_q, A_r):
        if ((A_p + A_q > A_r) and
            (A_q + A_r > A_p) and
            (A_r + A_p > A_q)):

                return True

        return False


# Attempt #2

class Solution:

    def solve(self, A):
        if len(A) < 3:
            return 0

        #   1. initialize index_R, index_Q, index_P, num_triangles
        index_P = total_num_triangles = 0
        index_Q = 1
        index_R = 2

        #   2. sort the array
        A.sort()

        #   3. starting at front == 2,
        while index_R < len(A):
            # 4. if A[index_Q], A[index_P], A[index_R] are triangles, raise count by 1

            if self.is_triangle(A[index_P], A[index_Q], A[index_R]):
                total_num_triangles += 1

            if self.move_index_R(index_P, index_Q, index_R, A):
                index_R += 1
                continue

            if self.move_index_Q(index_P, index_Q, index_R, A):
                index_Q += 1
                continue

            if self.move_index_P(index_P, index_Q, index_R, A):
                index_P += 1

        #   6. repeat the process until front is the size of Array
        return total_num_triangles

    def move_index_R(self, index_P, index_Q, index_R, A):
        if index_P == index_Q - 1 and index_Q == index_R - 1:
            return True

        if (index_P == index_Q -1) and self.is_triangle(A[index_P], A[index_Q], A[index_R]):
            return True if index_R < len(A) - 1 else False

        return False


    def move_index_Q(self, index_P, index_Q, index_R, A):
        if index_Q < index_R - 1:
            return True

        return False

    def move_index_P(self, index_P, index_Q, index_R, A):
        if index_P < index_Q - 1:
            return True
        return False


    def is_triangle(self, A_p, A_q, A_r):
        if ((A_p + A_q > A_r) and
            (A_q + A_r > A_p) and
            (A_r + A_p > A_q)):

                return True

        return False


if __name__ == '__main__':
    A_case_1 = [10, 2, 5, 1, 8, 12]

    expected_1 = 4

    solution_1 = Solution().solve(A_case_1)
    print(solution_1)

    assert expected_1 == solution_1