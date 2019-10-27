# Min Max Division
#
# given an array of integers A, partitioned into K sublists, create an algorithm
# that finds the smallest large sum of the partitions.
#
# input
#   - list of integers A
#   - integer (K - number of partitions)
#   - integer (M - upper bound of elements a sublist can have)
#
# output
#   - integer (the smallest large sum)
#
# constraints
#   - 0 <= K <= N
#   - N (the number of elements in A) and K are in range [1 ... 100,000]
#   - M is in between [0 and 10,000]
#   - value of each integer in A is in between [1 ... M]
#
#
# A = [2, 1, 5, 1, 2, 2, 2]
# K = 3
# M = 5
#
# [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
# [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
# [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
# [2, 1], [5, 1], [2, 2, 2] sum = 6
#
# output: 6
#
#
# cases
#   1. K == 0 --> not possible
#   2. K == 1 --> return sum(A)
#   4. K != 1
    #   4.1 len(A) == 1 --> return max(A)

# brainstorming solution
#   - solve using binary search
#       - initialize lower index, i and upper index j
#           lower index or i = max(A)
#           upper index or j = sum(A)

#       - as long as i and j don't cross
#           1. find the middle
#               half_distance = (j - i) // 2
#               mid = i + half_distance
#           2. check for solution
#               check for k, current_large_sum
#           3. if solution not satisfied, adjust the lower and uppder index
#               if k > K, i = mid + 1
#               if k <= K, j = mid - 1
#                   - also update smallest large sum (min(large_sum, current_large_sum))
#
#   - return the smallest_large sum

class Solution:
    def solve(self, K, M, A):
        large_sum = sum(A)

        i = max(A)
        j = large_sum

        if K == 1:
            return large_sum

        if len(A) == 1:
            return i

        while i <= j:
            half_distance = (j - i) // 2
            mid = i + half_distance

            k, current_large_sum = self.check(A, mid)

            if k > K:
                i = mid + 1
            else:
                j = mid - 1
                large_sum = min(large_sum, current_large_sum)

        return large_sum

    def check(self, A, mid):
        large_sum = 0
        k = 1

        partition_sum = A[0]
        index = 1

        while index < len(A):

            if partition_sum + A[index] > mid:
                large_sum = max(partition_sum, large_sum)
                partition_sum = A[index]
                k += 1
            else:
                partition_sum += A[index]

            index += 1

        large_sum = max(partition_sum, large_sum)

        return k, large_sum




# partition 1
# K = 3 M = 5
# [2, 1, 5, 1, 2, 2, 2] i = 5, j = 15, mid = 10
#              ^
# [2, 1, 5, 1][2, 2, 2]
#                    ^
#           k = 2
#           partition_sum = 9
#
# [2, 1, 5, 1][2, 2, 2]
#                    ^
#



if __name__ == '__main__':
    A_case_1 = [2, 1, 5, 1, 2, 2, 2]
    K_case_1 = 3
    M_case_1 = 5

    expected_1 = 6

    solution_1 = Solution().solve(K_case_1, M_case_1, A_case_1)
    print(solution_1)

    assert expected_1 == solution_1