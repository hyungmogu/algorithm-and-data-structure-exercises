# Ladder
#
# given two arrays A and B of same length, create an algorithm that returns
# a list of integers where each represents the f(A[index]) % 2 **(B[index])
# possibilities of climbing  the ladder given N = A[index]
#
# input
#   - two list of integers
#
# output
#   - list of integers
#
# constraint
#   - size of A and B, L is in between [1 ... 50,000]
#   - each element of A is in between [1 ... L]
#   - each element of B is in between [1 ... 30]
#   - two possibilities of climbing a ladder, climb up by 1 or by 2
#
#
#
# Example
# A = [4,4,5,5,1]
# B = [3,2,4,3,1]
#
# output = [5,1,8,0,1]
#
# why so?
#   - A[0] = 4 ==> the number of steps in a ladder
#       - The following possibilities exist
#           1. 1 + 1 + 1 + 1
#           2. 2 + 1 + 1
#           3. 1 + 2 + 1
#           4. 1 + 1 + 2
#           5. 2 + 2
#       - f(A[0]) = 5 % 2 ** (3) = 5 % 8 = 5
#
#   - A[1] = 4
#       -  f(A[1]) = 5 % 2 ** (2) = 5 % 4 = 1
#
#   - A[2] = 5
#       - f(A[2]) = 8 % 2 ** (5) = 8 % 32 = 8
#
#   - A[3] = 5
#       - f(A[3]) = 8 % 2 ** (3) = 8 % 8 = 0
#
#   - A[4] = 1
#       - f(A[4]) = 1 % 2 = 1
#
#
#
# brainstorming solution
#   1. initialize output (output = [None] * len(A)), L
#   2. for each element and index in A,
#   3. get combinations of climbing A[index] step and store in variable 'possibilities'
#   4. get f(A[index]) % 2 **(B[index]) and store in output[index]
#   5. return output
#
# O(N^2) time complexity and O(N) space complexity
#
# improved
#   1. initialize output (output = [None] * len(A)), L

#   2. calculate combinations in between [1 ... L]
#   3. for each element and index in A,
#   4. get combinations of climbing A[index] step and store in variable 'possibilities'
#   5. get f(A[index]) % 2 **(B[index]) and store in output[index]
#   6. return output
#


class Solution:
    def solve(self, A, B):
        #   1. initialize output (output = [None] * len(A)), L
        L = len(A)
        output = [None] * L
        index = 0

        if L == 1:
            return [1]

        #   2. calculate combinations in between [1 ... L]
        possibilities_list = self.get_possibilities_list(L)
        #   3. for each element and index in A,
        while index < len(A):
            #   4. get combinations of climbing A[index] step and store in variable 'possibilities'
            possibilities = possibilities_list[A[index]] % (2 ** (B[index]))
            #   5. get f(A[index]) % 2 **(B[index]) and store in output[index]
            index += 1

        #   6. return output
        return output

    def get_possibilities_list(self, L):
        # [1,1,2,3,5,8,...] --> fibonacci
        #      ^
        #   (1+1,2)
        #
        # 1. if L == 2, return [1,1]
        if L == 2:
            return [1,1]

        # 2. initialize dp (dp = [0] * (L+1)) and index == 2
        index_end = L + 1
        dp = [0] * index_end
        index = 2

        # 3. for index and element in dp upto (L + 1),
        while index < index_end:
            # 4. evaluate dp at index (dp[index] = dp[index - 1] + dp[index - 2])
            dp[index] = dp[index - 1] + dp[index - 2]
            index += 1

        # 5. once all done, return dp
        return dp


if __name__ == '__main__':
    A_case_1 = [4,4,5,5,1]
    B_case_1 = [3,2,4,3,1]

    expected_1 = [5,1,8,0,1]

    solution_1 = Solution().solve(A_case_1, B_case_1)

    assert expected_1 == solution_1