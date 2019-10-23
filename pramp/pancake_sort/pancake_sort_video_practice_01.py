# Pancake Sort
#
# given in array arr of integers, sort the elements using flip(arr, k) that
# flips the first k elements
#
#
# input
#    - array of integers
# output
#    - array of integers
#
# constraint
#   - flip can be used more than once
#
#
# arr = [1, 5, 4, 3, 2] --> is 2 < 5 --> YES --> flip
#                    x
#           ^
#
# flip # 1
# arr = [5, 1, 4, 3, 2]
#           x
#
# flip # 2
# arr = [2, 3, 4, 1, 5]
#
#
# arr = [2, 3, 4, 1, 5] --> is 1 < 4 --> YES --> flip
#                 x
#              ^
# flip # 1
# arr = [4, 3, 2, 1, 5]
#                 x
#
# flip # 2
# arr = [1, 2, 3, 4, 5]
#                 x
#
# arr = [1, 2, 3, 4, 5]  --> is 3 < 2 --> NO --> skip
#              x
# arr = [1, 2, 3, 4, 5]  --> is 2 < 1 --> NO --> skip
#           x
#
# Pseudocode
class Solution:
    def solve(self, arr):
        index = len(arr) - 1

        if len(arr) == 0:
            return arr

        if len(arr) == 1:
            return arr

        #   1. starting from the index of last element in arr, until index == 1
        while index > 0:
            #       1.1 find the index_maximum element in between the first element upto where index is
            index_maximum = self.getIndexMaximum(arr, index)

            #       1.2 if arr[index_maximum] > arr[index], flip(arr, index_maximum) and then flip(arr, index)
            if arr[index_maximum] > arr[index]:
                self.flip(arr, index_maximum)
                self.flip(arr, index)

            #       1.3 decrement index
            index -= 1

        #   2. return arr
        return arr

    def getIndexMaximum(self, arr, index_end):
        index = 0
        index_maximum = 0
        maximum = arr[index]

        while index < index_end:
            if arr[index] > maximum:
                maximum = arr[index]
                index_maximum = index

            index+= 1

        return index_maximum

    def flip(self, arr, k):
        # [1,2,3,4]
        #        x
        #  0 1 2 3
        #
        index = 0
        index_middle = k // 2

        while index <= index_middle:
            arr[index], arr[k - index] = arr[k - index], arr[index]
            index += 1

        return arr





if __name__ == '__main__':
    case_1 = [1]
    case_2 = [1,2]
    case_3 = [1,3,1]
    case_4 = [3,1,2,4,6,5]
    case_5 = [10,9,8,7,6,5,4,3,2,1]
    case_6 = [10,9,8,6,7,5,4,3,2,1,9,10,8,7,6,5,4,3,2,1,10,9,8,7,6,5,4,3,2,1]


    expected_1 = [1]
    expected_2 = [1,2]
    expected_3 = [1,1,3]
    expected_4 = [1,2,3,4,5,6]
    expected_5 = [1,2,3,4,5,6,7,8,9,10]
    expected_6 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]

    solution_1 = Solution().solve(case_1)
    solution_2 = Solution().solve(case_2)
    solution_3 = Solution().solve(case_3)
    solution_4 = Solution().solve(case_4)
    solution_5 = Solution().solve(case_5)
    solution_6 = Solution().solve(case_6)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4
    assert expected_5 == solution_5
    assert expected_6 == solution_6


