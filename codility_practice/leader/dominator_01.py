# Dominator
#
# An array A consisting of N integers is given. The dominator of array A is the
# value that occurs in more than half of the elements of A.
#
#
# For example, consider array A such that
#
#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely
# in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.
#
# Write a function
#
# def solution(A)
#
# that, given an array A consisting of N integers, returns index of any element
# of array A in which the dominator of A occurs. The function should return −1
# if array A does not have a dominator.
#
# For example, given array A such that
#
#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# the function may return 0, 2, 4, 6 or 7, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# cases
#   1. len(A) == 0
#   2. len(A) == 1
#   3. len(A) != 1
#

def get_element_frequency(A):
    number_frequency = {}

    for element in A:
        if element in number_frequency:
            number_frequency[element] += 1
        else:
            number_frequency[element] = 1

    return number_frequency

def get_dominator(number_frequency, A):
    keys = number_frequency.keys()

    is_dominator = len(A) // 2

    # 1. walk through each key
    for key in keys:
        # 2. if it satisfies the definition of dominator, return dominator
        is_dominator = number_frequency[key] > (len(A) // 2)

        if is_dominator:
            return key

    # 5.return None if doesn't exist
    return None

class Solution:
    def solve(self, A):
        if len(A) == 0:
            return -1

        if len(A) == 1:
            return 0

        # 1. for each number in A
        # 2. store count to number_frequency
        number_frequency = get_element_frequency(A)
        # 3. find dominator
        dominator = get_dominator(number_frequency, A)
        # 4. find the earliest index of dominator

        if dominator == None:
            return -1

        index = 0
        while index < len(A):
            if A[index] == dominator:
                return index

            index += 1

        return -1

if __name__ == '__main__':
    case_1 = [3,4,3,2,3,-1,3,3]
    case_2 = []
    case_3 = [1]
    case_4 = [1,1,1,1,2,2,2,2]

    expected_1 = 0
    expected_2 = -1
    expected_3 = 0
    expected_4 = -1

    solution_1 = Solution().solve(case_1)
    solution_2 = Solution().solve(case_2)
    solution_3 = Solution().solve(case_3)
    solution_4 = Solution().solve(case_4)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4
