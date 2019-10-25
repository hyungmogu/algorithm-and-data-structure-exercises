# Shifted Array Search
# A sorted array of distinct integers shiftArr is shifted to the left by an
# unknown offset and you don't have a pre-shifted copy of it. For instance, the
# sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.
#
# Given shiftArr and an integer num, implement a function shiftedArrSearch that
# finds and returns the index of num in shiftArr. If num isn't in shiftArr,
# return -1. Assume that the offset doesn't equal to 0 (i.e. assume the array is
# shifted at least once) or to arr.length - 1 (i.e. assume the shifted array isn't
# fully reversed).
#
# Explain your solution and analyze its time and space complexities.
#
# Example:
#
# input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
#                                                  # outcome of shifting
#                                                  # [2, 4, 5, 9, 12, 17]
#                                                  # three times to the left
#
# output: 3 # since it's the index of 2 in arr
# Constraints:
#
# [time limit] 5000ms
# [input] array.integer arr
# [input] integer num
# [output] integer
#
#
# pseudocode brute force solution
#   1. for each element in arr, compare with current_minimum
#   2. if arr[index] < minimum, then set minimum = arr[index], and index_minimum = index
#   3. return index_minimum
#
# time complexity is O(N) and spatial complexity is O(1)
#
# There is a better way to do this !!! Time complexity O(LGN)

# [9, 12, 17, 2, 4, 5] --> subtract 2 from everything in array --> [-7,-10,0,-2,-3 ]
#
# num =4
# [9, 12, 17, 2, 4, 5] --> [-5, -8, -13, 2, 0, -1]
#
# [2, 4, 5, 6, 9, 12, 17]
#           x
#
# while the indexes don't cross (index_floor + 1 < index_ceiling)
# 1. find the middle index
# 2. check if value at index_middle is the solution
#   2.1 if is solution, then return index_middle
# 3. if not solution and solution on left hand side, then set index_ceiling = index_middle
# 4. if not solution and solution on right hand side, then set index_floor = index_middle


class Solution:
    def solve(self, arr, num):
        index_floor = -1
        index_ceiling = len(arr)

        while index_floor + 1 < index_ceiling:
            # 1. find the middle index
            half_distance = (index_ceiling - index_floor) // 2
            index_middle = half_distance + index_floor

            # 2. check if value at index_middle is the solution
            #   2.1 if is solution, then return index_middle
            if arr[index_middle] == num:
                return index_middle

            # 3. if not solution and solution on left hand side, then set index_ceiling = index_middle
            if self.solution_exists_lhs(arr, index_floor, index_middle, num):
                index_ceiling = index_middle
            # 4. if not solution and solution on right hand side, then set index_floor = index_middle
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
    solution_4 = Solution().solve(case_4, 0)
    solution_5 = Solution().solve(case_5, 17)
    solution_6 = Solution().solve(case_6, 4)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4
    assert expected_5 == solution_5
    assert expected_6 == solution_6