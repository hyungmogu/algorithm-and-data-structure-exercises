# Find The Duplicates
#
# given two sorted arrays arr1 and arr2 with unique elements. Find, list of numbers
# that are in both arr1 and arr2
#
#  M ~ N
#  M >> N
#
# input
#   -  array of integers * 2
#
# Output
#   - array of integers
#
# constraint
#   - integers in arr1 and arr2 are unique
#   - numbers in arr1 and arr2 are sorted
#   - there is at least one element in both arr1 and arr2
#
#
# Brute Force Solution
#   1. we use two pointers to find all elements that are in both arr1 and arr2
#       -> because two for loops used --> O(N^2)
#
#
#

# Better Solution
#   1. using sets
#   2. two pointers, compare the two, increase the smaller index --> O(N + M)
#   3. binary search --> Time complexity O(N LOG M) where N << M (this is what we are going to work on), spatial complexity O(1)


# pseudocode
class Solution:
    def solve(self, arr1, arr2):
        output = []
        #   1. if len(arr1) > len(arr2), swap arr1 and arr2
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        #   2. for number in arr1:
        for number in arr1:
            #   1.1 if number is in arr2, then append number to output
            if self.valueInList(arr2, number):
                output.append(number)
        #   3. output

        return output


    # pseudocde - valueInList
    def valueInList(self, arr, number):
        #   1. initialize ceiling_index = len(arr) and floor_index = -1
        ceiling_index = len(arr)
        floor_index = -1

        #   2. while floor_index + 1 < ceiling_index:
        while floor_index + 1 < ceiling_index:
            #   3. find middle_index
            half_distance = (ceiling_index - floor_index) // 2
            middle_index = half_distance + floor_index

            #   4. if arr[middle_index] == number, return True
            if arr[middle_index] == number:
                return True

            #   5. if arr[middle_index] > number:
            if arr[middle_index] > number:
                ceiling_index = middle_index
            #       5.1 ceiling_index = middle_index
            #   6. if arr[middle_index] < number:
            if arr[middle_index] < number:
            #       6.1 floor_index = middle_index
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
