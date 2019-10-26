

# brute force solution
#   1. for each element and index in arr, check if solution exists from 0 to index
#       1.1 if does, return index
#   2. return -1 if all fails
#
# time complexity O(N^2) and spatial complexity of O(1)

# improved solution
#  1. initialize a set remaining_position_set with elements that needs to be crossed
#  2. for each element, remove the element from set
#  3. if length of set == 0, return index
#  4. return -1 if all fails


class Solution:
    def solve(self, A, X):
        if len(A) == 0:
            return -1

        remaining_position_set = set(range(1, X+1))
        index = 0

        while index < len(A):
            if A[index] in remaining_position_set:
                remaining_position_set.remove(A[index])

            if len(remaining_position_set) == 0:
                return index

            index +=1

        return -1


if __name__ == '__main__':
    A_case_1 = [1,3,1,4,2,3,5,4]
    X_case_1 = 5

    A_case_2 = []
    X_case_2 = -1

    A_case_3 = [1,3,1,4,2,3,5,4]
    X_case_3 = 10

    expected_1 = 6
    expected_2 = -1
    expected_3 = -1

    solution_1 = Solution().solve(A_case_1, X_case_1)
    solution_2 = Solution().solve(A_case_2, X_case_2)
    solution_3 = Solution().solve(A_case_3, X_case_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
