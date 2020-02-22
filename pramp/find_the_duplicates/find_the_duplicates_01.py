# Find The Duplicates
# Given two sorted arrays arr1 and arr2 of passport numbers, implement a function
# findDuplicates that returns an array of all passport numbers that are both in
# arr1 and arr2. Note that the output array should be sorted in an ascending order.

# Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases
# and analyze the time & space complexities of your solutions: M ~ N - the array
# lengths are approximately the same M >> N - arr2 is much bigger than arr1.

# Example:

# input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

# output: [3, 6, 7] # since only these three values are both in arr1 and arr2
# Constraints:

# [time limit] 5000ms

# [input] array.integer arr1

# 1 <= arr1.length <= 100
# [input] array.integer arr2

# 1 <= arr2.length <= 100
# [output] array.integer

# constraint
#   - The numbers are unique

#   1. when len(arr1) == len(arr2) --> one time pass! O(N) Time complexity and O(N) spatial complexity
#   2. when len(arr1) != len(arr2) --> use binary search on lengthier arr O(MlgN) where N >> M.

# Brute force solution
#   1. use two pointers and explore all combinations to find the maching values --> O(NM)

# Better solution
#   1. using set. (Time complexity of O(M) and spatial complexity O(N))
#       1.1. turn smaller arr into set.
#       1.2 travel the lengthier set and if value exist in set, then add to output
#
#   2. using binary search algorithm () <-- I will do this. since this is more difficult

# pseudocode
class Solution:
    def solve(self, arr1, arr2):
        #   1. if len(arr1) > len(arr2), swap the two
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        output = []

        #   2. for each element in smaller arr arr1, check using binary search algorithm to see if the value exists in the other arr
        for number in arr1:
            #   3. if the same value exists, then add to output, and continue
            if self.matchingValueExists(arr2, number):
                output.append(number)

        #   4. return output
        return output

    def matchingValueExists(self, arr, number):
        floor_index = -1
        ceiling_index = len(arr)

        if len(arr) == 1 and arr[0] == number:
            return True

        # 1. while the two pointers don't cross
        while floor_index + 1 < ceiling_index:
            # 2. find the middle index
            middle_index = (ceiling_index + floor_index) // 2

            # 3. if arr[middle_index] == number (is solution), then return True
            if arr[middle_index] == number:
                return True

            # 4. if arr[middle_index] > number:
            #    4.1 ceiling_index = middle_index
            if arr[middle_index] > number:
                ceiling_index = middle_index

            # 5. if arr[middle_index] < number:
            #   5.1 floor_index = middle_index
            if arr[middle_index] < number:
                floor_index = middle_index

        return False

#===========================================

if __name__ == '__main__':
    case_1_arr_1 = [11]
    case_1_arr_2 = [11]
    case_2_arr_1 = [1,3,5,9]
    case_2_arr_2 = [2,4,6,10]
    case_3_arr_1 = [1,2,3,5,6,7]
    case_3_arr_2 = [3,6,7,8,20]
    case_4_arr_1 = [1,2,3,5,6,7]
    case_4_arr_2 = [7,8,9,10,11,12]
    case_5_arr_1 = [10,20,30,40,50,60,70,80]
    case_5_arr_2 = [10,20,30,40,50,60]
    case_6_arr_1 = [10,20,30,40,50,60,70]
    case_6_arr_2 = [10,20,30,40,50,60,70]

    expected_1 = [11]
    expected_2 = []
    expected_3 = [3,6,7]
    expected_4 = [7]
    expected_5 = [10,20,30,40,50,60]
    expected_6 = [10,20,30,40,50,60,70]

    solution_1 = Solution().solve(case_1_arr_1, case_1_arr_2)
    solution_2 = Solution().solve(case_2_arr_1, case_2_arr_2)
    solution_3 = Solution().solve(case_3_arr_1, case_3_arr_2)
    solution_4 = Solution().solve(case_4_arr_1, case_4_arr_2)
    solution_5 = Solution().solve(case_5_arr_1, case_5_arr_2)
    solution_6 = Solution().solve(case_6_arr_1, case_6_arr_2)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4
    assert expected_5 == solution_5
    assert expected_6 == solution_6
