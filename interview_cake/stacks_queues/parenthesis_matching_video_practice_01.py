# Parenthesis Matching
#
# I like parentheticals (a lot).
#
# "Sometimes (when I nest them (my parentheticals) too much
# (like this (and this))) they get confusing."

# Write a function that, given a sentence like the one above, along with the
# position of an opening parenthesis, finds the corresponding closing parenthesis.

# Example: if the example string above is input with the number 10 (position
#  of the first parenthesis), the output should be 79 (position of the last
# parenthesis).
#
# Input
#   - string (setence)
#   - integer (location of left parenthesis)
#
# Output
#   - integer (location of right parenthesis)
#
#
# Constraints
#   - every left '(' parenthesis must have corresponding right ')' parenthesis
#
#
# Example
#
# "hello ((wor(ld)!!(!)))"
#        x
#        6              21
#
# left_parenthesis = 1
# right_parenthesis = -1
#
# property: the net sum of left_parenthesis (given value of +1) and matching right_parenthesis (given value of -1) is 0
#
#        v
# "hello ((wor(ld)!!(!)))"
#        x
#        6              21
#
# left_parenthesis = 1
# right_parenthesis = 0

#         v
# "hello ((wor(ld)!!(!)))"
#        x
#        6              21
#
# left_parenthesis = 2
# right_parenthesis = 0

#             v
# "hello ((wor(ld)!!(!)))"
#        x
#        6              21
#
# left_parenthesis = 3
# right_parenthesis = 0

#                v
# "hello ((wor(ld)!!(!)))"
#        x
#        6              21
#
# left_parenthesis = 3
# right_parenthesis = -1

#                   v
# "hello ((wor(ld)!!(!)))"
#        x
#        6              21
#
# left_parenthesis = 4
# right_parenthesis = -1

#                     v
# "hello ((wor(ld)!!(!)))"
#        x
#        6              21
#
# left_parenthesis = 4
# right_parenthesis = -2

#                      v
# "hello ((wor(ld)!!(!)))"
#        x
#        6              21
#
# left_parenthesis = 4
# right_parenthesis = -3

#                       v
# "hello ((wor(ld)!!(!)))"
#        x
#        6              21
#
# left_parenthesis = 4
# right_parenthesis = -4

# Brute force solution
    # 1. for each character with index = left_parenthesis_index,
    # left_parenthesis = 0
    # right_parenthesis = 0
    # index = left_parenthesis_index

    # while index < len(sentence):
    #     # 1.1 if character == '(', add the value of 'left_parenthesis' by 1
    #     # 1.2 if character == ')', and the value of 'right_parenthesis' by -1
    #     if sentence[index] == '(':
    #         left_parenthesis += 1

    #     if sentence[index] == ')':
    #         right_parenthesis -= 1

    #     # 1.3 if the sum of 'left_parenthesis' and 'right_parenthesis', return index
    #     if left_parenthesis + right_parenthesis == 0:
    #         return index

    # # 2. return -1 to indicate that matching parenthesis doesn't exist
    # return -1

#
# time complexity of O(N), spatial complexity of O(1)


class Solution:
    def parenthesisMatching(self, sentence, left_parenthesis_index):
        # 1. for each character with index = left_parenthesis_index,
        left_parenthesis = 0
        right_parenthesis = 0
        index = left_parenthesis_index

        while index < len(sentence):
            # 1.1 if character == '(', add the value of 'left_parenthesis' by 1
            # 1.2 if character == ')', and the value of 'right_parenthesis' by -1
            if sentence[index] == '(':
                left_parenthesis += 1

            if sentence[index] == ')':
                right_parenthesis -= 1

            # 1.3 if the sum of 'left_parenthesis' and 'right_parenthesis', return index
            if left_parenthesis + right_parenthesis == 0:
                return index

            index += 1

        # 2. return -1 to indicate that matching parenthesis doesn't exist
        return -1


if __name__ == '__main__':
    case = 'you are ((too be(au))(ti)ful)!!'

    opening_parenthesis_index_1 = 8
    opening_parenthesis_index_2 = 9
    opening_parenthesis_index_3 = 16
    expected_1 = 28
    expected_2 = 20
    expected_3 = 19

    solution_1 = Solution().parenthesisMatching(case, opening_parenthesis_index_1)
    solution_2 = Solution().parenthesisMatching(case, opening_parenthesis_index_2)
    solution_3 = Solution().parenthesisMatching(case, opening_parenthesis_index_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
