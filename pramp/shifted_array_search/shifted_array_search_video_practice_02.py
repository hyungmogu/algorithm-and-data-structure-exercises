
# shifted array search
#
# Given a sorted distinct array of integers shifted by an arbitrary amount,
# find and return the index of target element x
#
# return -1 if value not found in array
#
# [9, 12, 17, 2, 4, 5], num = 2
#
#
# output 3
#
#
# # [9, 12, 17, 2, 4, 5], num = 10
#
# output -1
#
#
# input
#   - list of integers (arr)
#   - integer (num)
#
# output
#   - integer
#
#
# Brute force solution
#   - use while loop.
#   - if arr[index] == num, return index
#   - return -1 when complete
#
# [9, 12, 17, 2, 4, 5] num =2
#             x
#
# Time complexity O(N) spatial complexity O(1)
#
#
# Improvement ? --> yes --> using binary search algorithm --> time complexity O(LG N), and spatial complexity --> O(1)
#
#   [9, 12, 17, 2, 4, 5] num =2 --> is 17 == 2 ? -> no --> solution is on lhs ? --> no --> index_floor = index_middle
#            x
#  -1        2          6
#
#  [9, 12, 17, 2, 4, 5] num =2  --> is 4 == 2 ? no --> solution is on lhs ? --> yes --> index_ceiling = index_middle
#           2          6
#                 x
#
#  [9, 12, 17, 2, 4, 5] num =2 --> is 2 == 2 ? yes --> return 3
#           2     4
#              x
#
class Solution:
    def solve(self, arr, num):
        index_ceiling = len(arr)
        index_floor = -1

        while index_floor + 1 < index_ceiling:
            # 1. find the index_middle
            half_distance = (index_ceiling - index_floor) // 2
            index_middle = index_floor + half_distance

            # 2. if arr[index_middle] == num, return index_middle
            if arr[index_middle] == num:
                return index_middle

            # 3. if num is on lhs, index_ceiling = index_middle
            if self.solution_on_lhs(arr, index_floor, index_middle, num):
                index_ceiling = index_middle
            # 4. if num is not on lhs, index_floor = index_middle
            else:
                index_floor = index_middle


        return -1

    def solution_on_lhs(self, arr, index_floor, index_middle, num):
        if index_floor < 0:
            index_floor = 0

        # 1. return ture if solution[index_floor] <= num and solution[index_middle] >= num
        if arr[index_floor] <= num and arr[index_middle] >= num:
            return True

        # 2. return true if solution[index_floor] > solution[index_middle]
        if arr[index_floor] <= num and arr[index_floor] > arr[index_middle]:
            return True

        # 3. return false
        return False


if __name__ == '__main__':
    case_1 = [2]
    case_2 = [1,2]
    case_3 = [0,1,2,3,4,5]
    case_4 = [1,2,3,4,5,0]
    case_5 = [9,12,1,2,4,5]
    case_6 = [9,12,17,2,4,5,6]
    case_7 = [9,12,17,18,4,5,6]

    expected_1 = 0
    expected_2 = 1
    expected_3 = 1
    expected_4 = 5
    expected_5 = 1
    expected_6 = 4
    expected_7 = 4

    solution_1 = Solution().solve(case_1, 2)
    solution_2 = Solution().solve(case_2, 2)
    solution_3 = Solution().solve(case_3, 1)
    print(solution_3)
    solution_4 = Solution().solve(case_4, 0)
    solution_5 = Solution().solve(case_5, 12)
    solution_6 = Solution().solve(case_6, 4)
    solution_7 = Solution().solve(case_6, 4)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4
    assert expected_5 == solution_5
    assert expected_6 == solution_6
    assert expected_7 == solution_7