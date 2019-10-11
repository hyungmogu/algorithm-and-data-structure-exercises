# Reverse Strings in place
#
# Write a function that takes a list of characters and reverses the letters in place.

# example (odd)
# [h, e, l, l, o] -> [o, l, l, e, h]
#  0  1  2  3  4
# example (even)
# [h, e, l, o] -> [o, l, e, h]
#  0  1  2  3
#
#
# PSEUDOCODE
#   1. if the word length is even
#   1.1. before it's at the middle (len(word) // 2), swap chars[i] with chars[-i]
#   1.2 return result
#
#   2. if the word length is even
#   2.1. before it's at the middle (len(word) // 2), swap chars[i] with chars[-i]
#   2.2 return result
#
#
# I can merge the two cases into one!!!
#
# PSEUDOCODE

class Solution:
    def reverseStringInPlace(self, chars):
        #   1. Find the length of word
        chars_length = len(chars)

        if chars_length == 0:
            return chars

        #   1.1. before it's at the middle (len(word) // 2), swap chars[i] with chars[-i]
        middle_point = len(chars) // 2
        index = 0

        while index < middle_point:
            chars[index], chars[-(index+1)] = chars[-(index+1)], chars[index]
            index += 1

        #   1.2 return result
        return chars


if __name__ == '__main__':
    case_1 = ['h', 'e', 'l', 'l', 'o']

    expected_1 = ['o', 'l', 'l', 'e', 'h']

    solution_1 = Solution().reverseStringInPlace(case_1)

    assert expected_1 == solution_1
