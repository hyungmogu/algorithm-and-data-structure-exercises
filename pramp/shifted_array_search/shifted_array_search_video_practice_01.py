"""
Here, Moe struggled with defining the condition for def solution_exists_lhs.

The solution below is incorrect, although all test cases are passed.

This is addressed in shifted_array_search_02.py
"""

# shifted array search
#
# given a sorted array but with the index of integers having shifted, find
# the index of target number 'num' by designing the most efficient algorithm
# possible
#
# Explain solution and analyze its time and space complexities
#
#
# Example
#
#
# input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2
#
# output: 3
#
# input
#   - array of integers
#   - integer (num)
# output
#   - integer
#
# constraints
#   - if the solution doesn't exist, return -1
#
#
# [9, 12, 17, 2, 4, 5], num = 2
#             x
#
# brute force algorithm
#   1. for each element & index in arr, if element == num, return index
#
# time complexity O(N), and spatial complexity is O(1)
#
# improved solution (binary search algorithm --> O(lg N))
#   -> how can we implement binary search algorithm to our solution?
#
# [9, 12, 17, 2, 4, 5]
#             x
#-1                   7
#
# pesudocode
class Solution:
    def solve(self, arr, num):
        index_ceiling = len(arr)
        index_floor = -1


        while index_floor + 1 < index_ceiling:
            #   1. find the middle point
            half_distance = (index_ceiling - index_floor) // 2
            index_middle = half_distance + index_floor

            #   2. check if the value at middle index is the solution
            #       2.1 if is the solution, return result
            if arr[index_middle] == num:
                return index_middle

            #   3. if not the solution, and solution exists on the left hand side, set index_ceiling = middle_index
            if self.solution_exists_lhs(arr, index_floor, index_middle, num):
                index_ceiling = index_middle

            #   4. if not the solution, and solution exists on the right hand side,set index_floor = middle_index
            else:
                index_floor = index_middle
        return -1

    def solution_exists_lhs(self, arr, index_floor, index_middle, solution):
        if index_floor < 0:
            index_floor = 0

        if solution >= arr[index_floor] and solution < arr[index_middle]:
            return True
        return False


if __name__ == '__main__':
    case_1 = [2]
    case_2 = [1,2]
    case_3 = [0,1,2,3,4,5]
    case_4 = [1,2,3,4,5,0]
    case_5 = [9,12,17,2,4,5]
    case_6 = [9,12,17,2,4,5,6]

    expected_1 = 0
    expected_2 = 1
    expected_3 = 1
    expected_4 = 5
    expected_5 = 2
    expected_6 = 4

    solution_1 = Solution().solve(case_1, 2)
    solution_2 = Solution().solve(case_2, 2)
    solution_3 = Solution().solve(case_3, 1)
    print(solution_3)
    solution_4 = Solution().solve(case_4, 0)
    solution_5 = Solution().solve(case_5, 17)
    solution_6 = Solution().solve(case_6, 4)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4
    assert expected_5 == solution_5
    assert expected_6 == solution_6