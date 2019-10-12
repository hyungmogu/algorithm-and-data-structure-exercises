# Reverse strings in place
#
# Write a function that takes a list of characters and reverses the letters in place.

# example (odd)
# [h, e, l, l, o] -> [o, l, l, e, h]
#  0  1  2  3  4
#
# step 1
# [h, e, l, l, o] --> [o, e, l, l, h]
#  x
#
# step 2
# [o, e, l, l, h] --> [o, l, l, e, h]
#     x
#        -3 -2 -1
# Brute Force
#
# Time complexity O(N/2) --> O(N),
# spatial complexity O(1) <-- inplace algorithm
#
#
# example (even)
# [h, e, l, o] -> [o, l, e, h]
#  0  1  2  3
#
# [m, e, e, e, o, w]
#  0  1  2  3  4  5

class Solution:
    def reverseStringInPlace(self, chars):
        #   1. find the length of the array
        char_size = len(chars)

        #   2. find the point where to stop interating ( len(chars) // 2)
        index_stop = len(chars) // 2

        #   3. for index from 0 to len(chars) // 2,
        #   3.1 swap chars[index] with chars[-index+1]
        index = 0
        while index < index_stop:
            chars[index], chars[-(index+1)] = chars[-(index+1)], chars[index]
            index += 1

        #   4. return chars to user
        return chars


if __name__ == '__main__':
    case_1 = ['h', 'e', 'l', 'l', 'o']
    case_2 = ['n','i','c','e']
    case_3 = []

    expected_1 = ['o', 'l', 'l', 'e', 'h']
    expected_2 = ['e','c','i','n']
    expected_3 = []

    solution_1 = Solution().reverseStringInPlace(case_1)
    solution_2 = Solution().reverseStringInPlace(case_2)
    solution_3 = Solution().reverseStringInPlace(case_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
