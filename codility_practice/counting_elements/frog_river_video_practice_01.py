# Frog river
#
# given an array of integers and integer value X, find the minimum index where
# it will contain all numbers/integers between 1 and X
#
# if no solution is found, return -1
#
# [1,3,1,4,2,3,5,4] X = 5
#
# output: 6
#
# input
#   - list of integers
#   - integer
#
# output
#   - integer
#
# known
#   - size of array N and value X is in range [1 ... 100,000]
#   - each element in array A falls in range [1 ... X]
#
#
#
# brute force solution
#   [1,3,1,4,2,3,5,4]
#    x
#   1. for each element and index in arr, check if required elements exist between arr at index == 0 and current index
#   2. if solution exists, then return index
#   3. if solution doesn't exist, increment index
#   4. if all fails, return -1
#
# time complexity O(N^2), spatial complexity O(1)
#
#
# improved solution --> uses set
# [1,3,1,4,2,3,5,4] {1,2,3,4,5}
# #1
#
# [1,3,1,4,2,3,5,4] {1,2,3,4,5} --> [1,3,1,4,2,3,5,4] {2,3,4,5} --> check if is solution --> no --> increment index by 1
#  x
#
# [1,3,1,4,2,3,5,4] {2,3,4,5} --> [1,3,1,4,2,3,5,4] {2,4,5} --> check if is solution --> no --> increment index by 1
#    x
#
# [1,3,1,4,2,3,5,4] {2,4,5} --> [1,3,1,4,2,3,5,4] {2,4,5} --> check if is solution --> no --> increment index by 1
#      x
#
# [1,3,1,4,2,3,5,4] {2,4,5} --> [1,3,1,4,2,3,5,4] {2,5} --> check if is solution --> no --> increment index by 1
#        x
#
# [1,3,1,4,2,3,5,4] {2,5} --> [1,3,1,4,2,3,5,4] {5} --> check if is solution --> no --> increment index by 1
#          x
#
# [1,3,1,4,2,3,5,4] {5} --> [1,3,1,4,2,3,5,4] {5} --> check if is solution --> no --> increment index by 1
#            x
#
# [1,3,1,4,2,3,5,4] {5} --> [1,3,1,4,2,3,5,4] {} --> check if is solution --> YES --> return result
#              x
#
class Solution:
    def solve(self, A, X):
        #   1. initialize set 'traveled_positions_set' containing elements from 1 to X
        traveled_positions_set = set(range(1, X+1))
        index = 0

        #   2. for each element,
        while index < len(A):
            #   2.1 if element exists in 'traveled_positions_set', remove number from the set
            if A[index] in traveled_positions_set:
                traveled_positions_set.remove(A[index])

            #   2.2 if is solution (len(traveled_positions_set) == 0), return index
            if len(traveled_positions_set) == 0:
                return index

            index += 1
        #   3. if all fails, return -1

        return -1


# Time complexity --> O(N) and spatial complexity O(N)
#
# cases
#   1. if len(A) == 0
#       - no need to consider
#   2. if len(A) == 1
#       - X > len(A)
#           - solution does not exist (doesn't have all elements in A)
#       - X == len(A)
#           - solution may exist (only when A contains required elements [1 ... X] --> [1])
#   3. if len(A) != 1
#       - X > len(A)
#           - solution does not exist (doesn't have all elements in A)
#       - X == len(A)
#           - solution may exist (only when A contains required elements [1 ... X])
#       - X < len(A)
#           - solution may exist (only when A contains required elements [1 ... X])

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

    solution_1 = Solution().solve(A_case_1, X_case_1)
    solution_2 = Solution().solve(A_case_2, X_case_2)
    solution_3 = Solution().solve(A_case_3, X_case_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
