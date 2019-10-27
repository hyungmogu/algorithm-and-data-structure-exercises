# Count Distinct Slices
#
# given a list of non-negative integers, find the total number of distinct slices
#
# Distinct slices represent tuple of two indexes (back, front) where A[front]
# is not a duplicate in betweeen back and front
#
# input
#   - list of integers (A)
#   - integer M (upper bound of elements in A)
# output
#   - integer (total number of distinct slices)
#
# Known
#   - if # of distinct slices > 1,000,000,000, return 1,000,000,000
#   - 0 <= back <= front <= N
#
# constraint
#   - N is an integer in range [1 ... 100,000]
#   - M is an integer in range [0 ... 100,000]
#   - each element in A is in range [0 ... M]
#
# Example
#
# [3] --> how many distinct slices ? slices = 1 {3}
#  + length between back and front
# [3,4] --> how many distinct slices ? slices = 3 {3}, {4}, {3,4}
#  + length between back and front
# [3,4,5] --> how many distinct slices ? slices = 6 {3}, {4}, {5}, {3,4}, {4,5}, {3,4,5}
#  + length between back and front
# [3,4,5,6] --> how many distinct slices ? slices = 10
#   {3},{4},{5},{6},{3,4},{4,5},{5,6},{3,4,5},{4,5,6},{3,4,5,6}
#
#
# [3] --> how many distinct slices ? slices = 1 {3}
#  + length between back and front
# [3,4] --> how many distinct slices ? slices = 3 {3}, {4}, {3,4}
#  + length between back and front
# [3,4,5] --> how many distinct slices ? slices = 6 {3}, {4}, {5}, {3,4}, {4,5}, {3,4,5}
#  + length between back and front (back = front = 3)
# [3,4,5,5] --> how many distinct slices? slices = 7 [{3}, {4}, {5}, {3,4}, {4,5}, {3,4,5}] < one set of distinct slices [{5}]
#
# [3,4,5,5,2] M = 6
#  0 1 2 3 4
#
# output: 9
#
# [3,4,5,5,2] {}
#  0 1 2 3 4
#  b
#  f
#
# [3,4,5,5,2] {3}
#  0 1 2 3 4
#  b
#    f
#
# [3,4,5,5,2] {3,4 }
#  0 1 2 3 4
#  b
#      f
#
# [3,4,5,5,2] {3,4 5} --> take out 3, and increment back by 1
#  0 1 2 3 4
#  b
#        f
#
# [3,4,5,5,2] {4 5} --> take out 4, increment back by 1
#  0 1 2 3 4
#    b
#        f
#
# [3,4,5,5,2] {5} --> take out 5, increment back by 1
#  0 1 2 3 4
#      b
#        f
#
# [3,4,5,5,2] {} --> take out 5, increment back by 1
#  0 1 2 3 4
#        b
#        f
#
#
# brainstorming solution
class Solution:
    def solve(self, M, A):
        #   0. if len(A) == 1, return 1
        if len(A) == 1:
            return 1

        #   1. initialize back, front, slices to be = 0, numbers_set = {}, LIMIT = 1,000,000,000
        back = front = slices = 0
        numbers_set = set()
        LIMIT = 1000000000

        #   2. while front < len(A),
        while front < len(A):

            #   3. if slices > LIMIT, return LIMIT
            if slices > LIMIT:
                return LIMIT

            #   4. if there is duplicate
            if A[front] in numbers_set:
                #       3.1 take out A[back] from numbers_set
                numbers_set.remove(A[back])

                #       3.2 increment back
                back += 1
                continue

            #   5. if not duplicate
            #       4.1 add A[front] to numbers_set
            #       4.2 caluclate size (size = back - front + 1)
            #       4.3 update slices (slices += size)
            #       4.4 increment front by 1
            numbers_set.add(A[front])
            size = front - back + 1
            slices += size

            front += 1

        #   6. return slices
        return slices


if __name__ == '__main__':
    A_case_1 = [3,4,5,5,2]
    M_case_1 = 6

    expected_1 = 9

    solution_1 = Solution().solve(M_case_1, A_case_1)
    print(solution_1)

    assert expected_1 == solution_1