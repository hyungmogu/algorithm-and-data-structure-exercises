# Passing Cars
#
# given array arr of 0 and 1s, where 0 represents cars traveling east, and 1
# represents car traveling west, create an algorithm that finds number of all
# pairs where 0 and 1 cross.
#
# if total number of cars crossing is > 1,000,000,000, return -1
#
# input
#   - a list of integers
# output
#   - integer
#
# constraints
#   - N , number of elements in arr, is in between [1 ... 100,000]
#
# Example
# [0,1,0,1,1]
#  0 1 2 3 4
#
#   -> [(0,1),(0,3),(0,4),(2,3),(2,4)]
#
# Output: 5
#
#
# cases
#   1. len(arr) == 0 -> no need to consider. len(arr) >= 1
#   2. len(arr) == 1 -> return 0
#   3. len(arr) != 1
#       3.1 total number of crossing <= 1,000,000,000
#       3.2 total number of crossing > 1,000,000,000 --> return -1
#
#
# brute force solution
#   1. initialize LIMIT = 1,000,000,000
#   2. for each element 0 in arr,
#       1.1 for any 1 after index pair up (i.e. (0,1)) and store in list 'output'
#   3. count 'output' and store in 'crossing_total'
#   4. if crossing_total > LIMIT, return -1
#   5. return crossing_total
#
#   time complexity O(N^2) and spatial complexity O(N^2)
#
# improved solution
# [0,1,0,1,1] -> output = total sum of 1s after each 0
#
#   1. if len(A) == 1, return 0
#   2. initialize cars_traveling_west_total = 0, crossings_total = 0
#   3. count total number of 1s and store in 'cars_traveling_west_total'
#   4. for each element in arr
#   5. if element == 0, add 'crossings_total' by cars_traveling_west_total
#   6. if element == 1, subtract 'cars_traveling_west_total' by 1
#   7. if crossing_total > LIMIT, return -1
#   8. return crossing_total
#
# output: 5
#
# Time complexity O(N), spatial complexity O(1)

class Solution:
    def solve(self, A):
        #   1. if len(A) == 1, return 0
        if len(A) == 1:
            return 0

        #   2. initialize cars_traveling_west_total = 0, crossings_total = 0
        cars_traveling_west_total = 0
        crossings_total = 0
        LIMIT = 1000000000

        #   3. count total number of 1s and store in 'cars_traveling_west_total'
        for number in A:
            if number == 1:
                cars_traveling_west_total += 1

        #   4. for each element in arr
        for number in A:

            #   5. if element == 0, add 'crossings_total' by cars_traveling_west_total
            if number == 0:
                crossings_total += cars_traveling_west_total
            else:
            #   6. if element == 1, subtract 'cars_traveling_west_total' by 1
                cars_traveling_west_total -= 1

        #   7. if crossing_total > LIMIT, return -1
        if crossings_total > LIMIT:
            return - 1

        #   8. return crossing_total
        return crossings_total


if __name__ == '__main__':
    case_1 = [1]
    case_2 = [0,0]
    case_3 = [1,1]
    case_4 = [0,1,0,1,1]

    expected_1 = 0
    expected_2 = 0
    expected_3 = 0
    expected_4 = 5

    solution_1 = Solution().solve(case_1)
    solution_2 = Solution().solve(case_2)
    solution_3 = Solution().solve(case_3)
    solution_4 = Solution().solve(case_4)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4