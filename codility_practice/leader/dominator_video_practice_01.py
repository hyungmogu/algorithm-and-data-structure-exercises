# Dominator
#
# given an array of integers arr containing N many elements, find the index of element
# that is the dominator of the array
#
# The definition of dominator is the element that contains more than half of the total elements
#
# [3,4,3,2,3,-1,3,3] --> the dominator is 3 because 5 are present in 8 total --> return index 0
#
# if solution doesn't exist, return -1
#
# input
#   - list of integers
#
# output
#   - integer (is the index of dominator)
#
# constraints / known
#   - dominator is the element with count more than half of the length of array
#
#   - the size of N is in [0 ... 100,000]
#   - element is of range [-INT.MAX, INT.MAX]
#
# cases
#   1. len(A) == 0 --> return - 1
#   2. len(A) == 1 --> return 0
#   3. len(A) != 1
#
# Brainstorming
#
# []
#
# [1]
#
# [3,3,1,1,2,2] --> is not dominator --> return -1
#
# [3,4,3,2,3,-1,3,3] {} --> [3,4,3,2,3,-1,3,3] {3: 5, 4: 1, 2: 1, -1: 1} --> 3 has count > half of array (4) --> return 0
#  x                                          x
#
class Solution:
    def solve(self, A):
        # 1. if len(A) == 0, return -1
        if len(A) == 0:
            return -1
        # 2. if len(A) == 1, return 0
        if len(A) == 1:
            return 0

        # 3. count frequency of each number and store in dictionary 'number_frequency'
        number_frequency= self.get_number_frequency(A)

        # 4. get dominator
        dominator = self.get_dominator(number_frequency, A)

        # 5. if dominator doesn't exist, return -1
        if dominator == None:
            return -1

        # 6. find earliest index of the domninator
        index = 0
        while index < len(A):
            if A[index] == dominator:
                return index
            index += 1

        # 7. return index
        return -1
        # Time complexity O(N), spatial complexity O(N)

    def get_number_frequency(self, A):
        number_frequency = {}

        for number in A:
            if number in number_frequency:
                number_frequency[number] += 1
            else:
                number_frequency[number] = 1

        return number_frequency

    def get_dominator(self, number_frequency, A):

        for key in number_frequency.keys():

            is_dominator = number_frequency[key] > (len(A) // 2)
            if is_dominator:
                return key

        return None

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
