# Pancake Sort

# given an array arr, and flip(arr, k) that flips the first k elements,
# create a method that sorts and returns sorted array

# Example
# [1,3,1] -> biggest before x = 3
#      x
#
# [3,1,1]
#
# [1,1,3] flip!
#
#
# cases
#   1. when the arr is empty
#   2. when the arr has length == 1
#   3. when the arr has length > 1


# pseudocode
#   1. if arr is empty, then return arr
#   2. if arr has length == 1, then return arr
#   3. if arr has length > 1,
#       3.1 starting index from the last element in the arr, find maximum elements in [:index]
#       3.2 if maximum > last_element, then flip to first then to last
#       3.2 decrement index
#   4. if index == 1, then terminate
#
#   return arr


class Solution:
    def solve(self, arr):
        #   1. if arr is empty, then return arr
        if len(arr) == 0:
            return arr

        #   2. if arr has length == 1, then return arr
        if len(arr) == 1:
            return arr

        index = len(arr) - 1

        while index > 0:
            #   3. if arr has length > 1,
            #       3.1 starting index from the last element in the arr, find maximum elements in [:index]
            maximum, index_maximum = self.get_index_maximum(arr, index)
            #       3.2 if maximum > last_element, then flip to first then to last
            if maximum > arr[index]:
                self.flip(arr, index_maximum)
                self.flip(arr, index)

            print(arr)
            index -= 1

        return arr

    def get_index_maximum(self, arr, index_end):
        index = 0
        index_maximum = 0
        maximum = arr[index]

        while index < index_end:
            if maximum < arr[index]:
                maximum = arr[index]
                index_maximum = index
            index += 1

        return maximum, index_maximum

    def flip(self, arr, k):
        index = 0
        index_end = k // 2

        while index <= index_end:
            arr[index], arr[k - index] = arr[k - index] , arr[index]
            index += 1

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
    print(solution_3)
    solution_4 = Solution().solve(case_4)
    solution_5 = Solution().solve(case_5)
    solution_6 = Solution().solve(case_6)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4
    assert expected_5 == solution_5
    assert expected_6 == solution_6


