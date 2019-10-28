# Small Frog
#
# A small frog wants to get from position 0 to k (1 <= k <= 10 000). The frog can
# jump over any one of n fixed distances s0, s1, . . . , sn−1 (1 <= si <= k). The goal is to count the
# number of different ways in which the frog can jump to position k. To avoid overflow, it is
# sufficient to return the result modulo q, where q is a given number

#
# input
#   - list of integers (s0 ... sn-1)
#   - intger (k - the tatget position)
#   - integer (q - number to perform modulo)
#
# output
#   - integer (total number of different moves at q)
#
# constraint
#   - 1 <= k <= 10,000
#   - 1 <= s_i <= k
#
# knwon
#   - dp[0] is always 1 --> 1 way to travel itself
#
# cases
#   1. where k == 1 --> return 1
#   2. where k != 1

#
#
#  this happens to be the sum of all subsequent moves (dp[index_i] += dp[index_i] - s[index_j]]) where index_j < len(S)
#   - this can only work if index_i >= s[index_j]
#
# brainstorming solution
class Solution:
    def solve(self, K, S, q):
        #   1. if k == 1, return 1
        if K == 1:
            return 1

        #   2. intialize index_i = 0 and dp (dp = [1] + [0] * k)
        index_i = 0
        dp = [1] + [0] * K

        #   3. while index_i < k + 1, and while index_j < len(S)
        while index_i < (K+1):
            index_j = 0
            while index_j < len(S):
                if index_i >= S[index_j]:
                    dp[index_i] += dp[index_i - S[index_j]]

                index_j += 1

            dp[index_i] %= q

            index_i +=1

        #   4. compute dp at index_i
        #   5. return dp[-1]
        return dp[-1]

#
# this has time complexity of O(k*N) and spatial complexity O(1)


if __name__ == '__main__':
    K_case_1 = 3
    S_case_1 = [1,2]
    q_case_1 = 10

    K_case_2 = 1
    S_case_2 = [1,2]
    q_case_2 = 10

    expected_1 = 3
    expected_2 = 1

    solution_1 = Solution().solve(K_case_1, S_case_1, q_case_1)
    solution_2 = Solution().solve(K_case_2, S_case_2, q_case_2)

    assert expected_1 == solution_1
    assert expected_2 == solution_2

