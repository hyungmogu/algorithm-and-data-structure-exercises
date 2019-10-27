# Min Max Division
#
# You are given integers K, M and a non-empty array A consisting of N integers.
# Every element of the array is not greater than M.
#
# You should divide this array into K blocks of consecutive elements. The size
# of the block is any integer between 0 and N. Every element of the array should
# belong to some block.
#
# The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum
# of empty block equals 0.
#
# The large sum is the maximal sum of any block.
#
# For example, you are given integers K = 3, M = 5 and array A such that:
#
#   A[0] = 2
#   A[1] = 1
#   A[2] = 5
#   A[3] = 1
#   A[4] = 2
#   A[5] = 2
#   A[6] = 2
# The array can be divided, for example, into the following blocks:
#
# [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
# [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
# [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
# [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
# The goal is to minimize the large sum. In the above example, 6 is the minimal
# large sum.
#
# Write a function:
#
# def solution(K, M, A)
#
# that, given integers K, M and a non-empty array A consisting of N integers,
# returns the minimal large sum.
#
# For example, given K = 3, M = 5 and array A such that:
#
#   A[0] = 2
#   A[1] = 1
#   A[2] = 5
#   A[3] = 1
#   A[4] = 2
#   A[5] = 2
#   A[6] = 2
# the function should return 6, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N and K are integers within the range [1..100,000];
# M is an integer within the range [0..10,000];
# each element of array A is an integer within the range [0..M].

# ============================
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
#
# Input
#   - list of integers (A)
#   - integer (K - the number of partitions / sublist)
#   - intger (M - the upper bound of the number of elements in sublist)
#
# output
#   - integer (the largest minimal sum)
#
# constraints
#   - 0 <= K and K <= N
#   - N and K in range [1 ... 100,000]
#
# cases
#   1. K = 0 --> doesn't exit
#   1. K = 1 --> sum(A)
#   2. 1 < K and K < N
#   3. K = N --> max(A)
#
# =========================
class Solution:
    def solve(self, K, M, A):
        #   1. initialize index_floor and index_ceiling (index_floor = max(A), index_ceiling = sum(A))
        large_sum = sum(A)
        i = max(A)
        j = large_sum

        N = len(A)

        if K == 1:
            return large_sum

        if K == N or len(A) == 1:
            return i

        #   2. while i and j don't cross
        while i <= j:
            #   3. find mid
            half_distance = (j - i) // 2
            mid =  i + half_distance

            #   4. check solution (getting the current number of paritions k. and current maximum, and checking to see if partition is correct)
            k, current_large_sum = self.check(A, mid)

            #   5. if current partition k > K,
            #       4.1 set index_floor = index_mid + 1
            #   6. if current partition is k <= K,
            #       5.1 set j = mid - 1
            #       5.2 update smallest large_sum (min(large_sum, current_large_sum))
            if k > K:
                i = mid + 1
            else:
                j = mid - 1
                large_sum = min(large_sum, current_large_sum)

        return large_sum

    # time complexity

    def check(self, A, mid):
        k = 1
        large_sum = 0
        index = 1

        partition_sum = A[0]

        while index < len(A):
            if partition_sum + A[index] > mid:
                large_sum = max(large_sum,partition_sum)
                partition_sum = A[index]
                k += 1
            else:
                partition_sum += A[index]

            index += 1

        # update it one last time for the last element
        large_sum = max(large_sum,partition_sum)

        # write your code in Python 3.6
        return k, large_sum



if __name__ == '__main__':
    A_case_1 = [2, 1, 5, 1, 2, 2, 2]
    K_case_1 = 3
    M_case_1 = 5

    expected_1 = 6

    solution_1 = Solution().solve(K_case_1, M_case_1, A_case_1)

    assert expected_1 == solution_1