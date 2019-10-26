# permutation missing element
#
# given an array containing N unique integers with each element ranging between
# [1 ... (N+1)], find the missing element
#
#  [2, 3, 1, 5]
#
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
#
# output: 4
#
# input
#   - list of integers
#
# output
#   - integer
#
# known
#   - N --> the size of list
#   - integer in arr is in between [1 ... (N + 1)]
#   - the size of arr is in between [0 ... 100,000]
#   - element in arr are unique
#
# case
#   1. if len(A) == 0, return 1
#   2. if len(A) != 0
#
# [1 ... 5]
#
# [2,3,1,5]
#
#
# Brute force solution
#   1. for each element, loop through arr and check if element doesn't exist
#       1.1 if it doesn't eixst, then return value
#
#   2. don't return anything after reaching the end
#
# time complexity O(N^2), spatial complxity O(1)

class Solution:
    def solve(self, A):
        # improved solution
        #   - use set
            if len(A) == 0:
                return 1

        #   2. turn arr to a set
            set_A = set(A)
        #   3. for each element in [1 ... (N+1)], if element doesn't exist in set, return value
            index = 1

            while index <= len(A) + 1:
                if index not in set_A:
                    return index

                index += 1

if __name__ == '__main__':
    case_1 = []
    case_2 = [1,3]
    case_3 = [2,3,1,5]
    case_4 = [2,3,1,4]
    case_5 = [2]

    expected_1 = 1
    expected_2 = 2
    expected_3 = 4
    expected_4 = 5
    expected_5 = 1

    solution_1 = Solution().solve(case_1)
    solution_2 = Solution().solve(case_2)
    solution_3 = Solution().solve(case_3)
    solution_4 = Solution().solve(case_4)
    solution_5 = Solution().solve(case_5)

    assert solution_1 == expected_1
    assert solution_2 == expected_2
    assert solution_3 == expected_3
    assert solution_4 == expected_4
    assert solution_5 == expected_5