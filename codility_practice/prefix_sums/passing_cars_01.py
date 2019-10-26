# A non-empty array A consisting of N integers is given. The consecutive elements of
# array A represent consecutive cars on a road.

# Array A contains only 0s and/or 1s:

# 0 represents a car traveling east,
# 1 represents a car traveling west.
# The goal is to count passing cars. We say that a pair of cars (P, Q), where
# 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling
# to the west.

# For example, consider array A such that:

#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the number of pairs of
# passing cars.

# The function should return −1 if the number of pairs of passing cars exceeds
# 1,000,000,000.

# For example, given:

#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# the function should return 5, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer that can have one of the following values: 0, 1.


# ========= Solution =========


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# cases
#   1. N == 0 --> Not possible
#   2. N == 1 --> return 0
#   3. N != 1
#       3.1 # of 1 == 0 --> return 0
#       3.2 # of 1 != 0
#           3.2.1 # of 1 == len(arr) -->return 0
#           3.2.2 # of 1 != len(arr)
#               3.2.2.1 total numbers of cars passing > 1,000,000,000 --> return -1
#
# Brute force solution
#   1. for each 0, find all 1
#   2. store its index in output
#   3. return len(output)

# Improved solution
#   1. initialize current_total_1 = 0
#   2. count all 1 in arr and store in 'current_total_1'
#   3. for each element in arr
#       2.1 if element == 0, add total by the current_total_1
#       2.2 if element != 0, subtract current_total_1 by 1
#
# time complexity O(N), spatial complexity O(1)

class Solution:
    def solve(A):
        # write your code in Python 3.6

        #   1. initialize current_total_1 = 0
        current_total_1 = 0
        total = 0
        LIMIT = 1000000000

        if len(A) == 1:
            return 0

        #   2. count all 1 in arr and store in 'current_total_1'
        for number in A:
            if number == 1:
                current_total_1 += 1

        if current_total_1 == len(A):
            return 0

        #   3. for each element in arr
        for number in A:
            #       2.1 if element == 0, add total by the current_total_1
            if number == 0:
                total += current_total_1

            #       2.2 if element != 0, subtract current_total_1 by 1
            else:
                current_total_1 -= 1

        if total > LIMIT:
            return -1

        return total

    # time complexity O(N), spatial complexity O(1)


if __name__ == '__main__':
    case_1 = []
    case_2 = [1]
    case_3 = [0,1]
    case_4 = [1,1]
    case_5 = [0,0]
    case_6 = [0,1,0,1,1]

    expected_1 = 0
    expected_2 = 0
    expected_3 = 1
    expected_4 = 0
    expected_5 = 0
    expected_6 = 5

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