# Cyclic Rotation
#
# Given array A = [3, 8, 9, 7, 6] and integer value K, design an algorithm
# that returns the elements in A shifted by amount k
#
# Example
#
#  A = [3, 8, 9, 7, 6]
#  K = 3
#
# output: [9, 7, 6, 3, 8]
#
#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
#
# Example 2
#
#     A = [0, 0, 0]
#     K = 1
#
# output: [0, 0, 0]
#
# Example 3
#
#     A = [1, 2, 3, 4]
#     K = 4
#
# output: [1,2,3,4]
#
#
# inputs
#   - an array of integers
#   - integer
#
# output
#   - an array of integers
#
# constraint
#   - N and K are integers in range [0 ... 100]
#   - each element in array A is an integer in range [-1000 ... 1000]
#   - we don't need to focus on the efficiency of the problem. correctness suffices
#
#
#  [3, 8, 9, 7, 6] K =3
#
#
#  [3, 8, 9, 7, 6] --> [9, 7, 6, 3, 8] ==> putting an element at index in index + K in another array!!!
#   0                            3
#
#  [3, 8, 9, 7, 6] --> [9, 7, 6, 3, 8] ==> putting an element at index in ( index + K ) % len(A) in another array!!!
#            3             1
#
# [3, 8, 9, 7, 6] , [-,-,-,-,-]
#
# # 1
# [3, 8, 9, 7, 6] , [-,-,-,3,-]
#  x
#
# # 2
# [3, 8, 9, 7, 6] , [-,-,-,3,8]
#     x
#
# # 3
# [3, 8, 9, 7, 6] , [9,-,-,3,8]
#        x
#
# # 4
# [3, 8, 9, 7, 6] , [9,7,-,3,8]
#           x
#
# # 4
# [3, 8, 9, 7, 6] , [9,7,6,3,8]
#              x
#
# Pseudocode
class Solution:
    def solve(self, A, K):
        #   1. initialize output array ([None] * len(A))

        if len(A) == 0 or len(A) == 1 or K == len(A):
            return A

        output = [None] * len(A)

        #   2. for each element, index in A. put element in output at position (index + K) % len(A)
        index = 0
        while index < len(A):
            index_new = (index + K) % len(A)
            output[index_new] = A[index]

            index += 1

        return output
        #   3. return output
#
# time complexity O(N) and spatial complexity O(N)

if __name__ == '__main__':
    A_case_1 = []
    K_case_1 = 100
    A_case_2 = [1]
    K_case_2 = 2
    A_case_3 = [3, 8, 9, 7, 6]
    K_case_3 = 3
    A_case_4 = [1,2,3,4]
    K_case_4 = 4

    expected_1 = []
    expected_2 = [1]
    expected_3 = [9, 7, 6, 3, 8]
    expected_4 = [1,2,3,4]

    solution_1 = Solution().solve(A_case_1, K_case_1)
    solution_2 = Solution().solve(A_case_2, K_case_2)
    solution_3 = Solution().solve(A_case_3, K_case_3)
    solution_4 = Solution().solve(A_case_4, K_case_4)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4
