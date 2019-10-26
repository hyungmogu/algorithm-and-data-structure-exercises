# permutation_missing_element
#
# An array A consisting of N different integers is given. The array contains
# integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Your goal is to find that missing element.

# Write a function:

# def solution(A)

# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

# ================ solution ====================

#
# brute force solution
#   1. for each element in [1 ... N+1], check if element in A
#   2. if element not in A, return value
#
#   Time complexity O(N^2) and spatial complexity O(1)
#
# improved solution
#   - using sets
#   1. store all elements in A to set
#   2. for each element in [1 ... N+1], check if element in A
#   3. if element not in A, return value
#
#   Time complexity O(N) and spatial complexity O(N)
#
class Solution:
    def solve(self, A):
        #   1. store all elements in A to set
        set_A = set(A)
        value = 1

        if len(A) == 0:
            return value

        #   2. for each element in [1 ... N+1], check if element in A
        while value <= len(A) + 1:
            if value not in set_A:
                return value

            value += 1
        #   3. if element not in A, return value


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