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
#
# Constraints
#   - every left '(' parenthesis must have corresponding right ')' parenthesis
#
# Example
# "hello (world)"
#        6     12
# Notice the net sum of left bracket '(' (say +1) and correspoinding right bracket ')' (say -1) should be zero
#
# Example 2.1
#                              v
# "you are ((too be(au))(ti)ful)!!"
#          x
#
# left bracket: 1
# right bracket: 0
#                              v
# "you are ((too be(au))(ti)ful)!!"
#           x
#
# left bracket: 2
# right bracket: 0
#                              v
# "you are ((too be(au))(ti)ful)!!"
#                  x
#
# left bracket: 3
# right bracket: 0
#
#                              v
# "you are ((too be(au))(ti)ful)!!"
#                     x
#
# left bracket: 3
# right bracket: 1
#
#                              v
# "you are ((too be(au))(ti)ful)!!"
#                      x
#
# left bracket: 3
# right bracket: 2
#
#                              v
# "you are ((too be(au))(ti)ful)!!"
#                       x
#
# left bracket: 4
# right bracket: 2
#
#                              v
# "you are ((too be(au))(ti)ful)!!"
#                          x
#
# left bracket: 4
# right bracket: 3
#
#                              v
# "you are ((too be(au))(ti)ful)!!"
#                              x
#
# left bracket: 4
# right bracket: 4
#
#
# Brute force solution

class Solution:
    def parenthesisMatching(self, sentence, opening_parenthesis_index):
        # 1. for each character in 'sentence',
        index = opening_parenthesis_index
        left_parenthesis = 0
        right_parenthesis = 0

        while index < len(sentence):
            # 1.1 if character is '(', add value of 'left_parenthesis' by 1
            if sentence[index] == '(':
                left_parenthesis += 1

            # 1.2 if character is ')', add value of 'right_parenthesis' by -1
            if sentence[index] == ')':
                right_parenthesis -= 1

            # 1.3 if 'left_parenthesis' + 'right_parenthesis' is 0, then return index
            if left_parenthesis + right_parenthesis == 0:
                return index

            index += 1

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
