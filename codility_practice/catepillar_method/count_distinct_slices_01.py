# Count Distinct Slices
#
# An integer M and a non-empty array A consisting of N non-negative integers are
# given. All integers in array A are less than or equal to M.
#
# A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array
# A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct
# slice is a slice consisting of only unique numbers. That is, no individual number
# occurs more than once in the slice.
#
# For example, consider integer M = 6 and array A such that:
#
#     A[0] = 3
#     A[1] = 4
#     A[2] = 5
#     A[3] = 5
#     A[4] = 2
# There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1),
# (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).
#
# The goal is to calculate the number of distinct slices.
#
# Write a function:
#
# def solution(M, A)
#
# that, given an integer M and a non-empty array A consisting of N integers,
# returns the number of distinct slices.
#
# If the number of distinct slices is greater than 1,000,000,000, the function
# should return 1,000,000,000.
#
# For example, given integer M = 6 and array A such that:
#
#     A[0] = 3
#     A[1] = 4
#     A[2] = 5
#     A[3] = 5
#     A[4] = 2
# the function should return 9, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# M is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..M].

# ======== solution ========

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
#
# pseudocode (using the catepillar method)
#   1. if len(A) == 1, return 1
#   2. for each back pointer is less than len(A) and back + front < len(A)
#   3. if duplicate exists,
#       2.1 reduce size by 1
#       2.2 increment back by 1
#   4. determine size (size = front - back + 1)
#   5. update slices (slices += size)
#   6. add number to numbers_set
#   7. increment front by 1
#
#
# Attempt # 1
class Solution:
    def solve(self, M, A):
        #   1. initialize index_i to be 0 and index_j to be index_i and set to be empty and slices = 0
        if len(A) == 1:
            return 1

        index_i = 0
        slices = 0
        LIMIT = 1000000000

        while index_i < len(A):
            index_j = index_i
            numbers_set = set()

            #   2. while index_i < len(A) and index_j < len(A)
            #   3. if A[index_j] not in numbers_set,
            #       3.1 add number to numbers_set
            #       3.2 increment 'slices' by 1
            #       3.3 increment index_j by 1 and continue
            #   4. otherwise increment index_i by 1 and continue
            while index_j <len(A):

                if A[index_j] in numbers_set:
                    break

                slices += 1

                # if slices greater than 1,000,000,000 return 1,000,000,000
                if slices == LIMIT:
                    return LIMIT

                numbers_set.add(A[index_j])
                index_j += 1

            index_i += 1
        return slices


# Attempt # 2
class Solution:
    def solve(self, M, A):
        back = front = slices = 0
        numbers_set = set()
        LIMIT = 1000000000

        #   1. if len(A) == 1, return 1
        if len(A) == 1:
            return 1
        #   2. for each back pointer is less than len(A) and back + front < len(A)
        while front < len(A):
            if slices > LIMIT:
                return LIMIT

            #   3. if duplicate exists,
            if A[front] in numbers_set:
                numbers_set.remove(A[back])
                #       2.1 reduce size by 1
                size -= 1
                #       2.2 increment back by 1
                back += 1

                continue

            #   4. determine size (size = front - back + 1)
            size = front - back + 1
            #   5. update slices (slices += size)
            slices += size

            #   6. add number to numbers_set
            numbers_set.add(A[front])

            #   7. increment front by 1
            front += 1

        return slices



if __name__ == '__main__':
    A_case_1 = [3,4,5,5,2]
    M_case_1 = 6

    expected_1 = 9

    solution_1 = Solution().solve(M_case_1, A_case_1)

    assert expected_1 == solution_1