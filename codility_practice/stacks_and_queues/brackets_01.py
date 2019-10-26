# Brackets
#
# A string S consisting of N characters is considered to be properly nested if
# any of the following conditions is true:
#
# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.
#
# Write a function:
#
# def solution(S)
#
# that, given a string S consisting of N characters, returns 1 if S is properly
# nested and 0 otherwise.
#
# For example, given S = "{[()()]}", the function should return 1 and given
# S = "([)()]", the function should return 0, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}"
# and/or ")".

# ========= Solution ==========


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# input
#   - string
# output
#   - integer (0 or 1)
#
# knowns
#   1. S consists of the characters '(', '{', '[', ']', '}', ')'
#   2. S is properly nested if or every right brackets of all types has its corresponding matching pairs
#   3. with a bracket there has to exist matching pairs of brackets if of another bracket type
#
# example
# "{[()()]}" --> properly nested --> return 1
# ""([)()]" --> not properly nested --> return 0
#
# pseudocode
#   1. for each element
#   2. if element is left handed bracket, push to stack
#   3. if element is right handed bracket, pop the element
#       3.1 if the popped element is not the opposite pair of the right handed bracket, return 0
#   4. otherwise, return 1
#
# time complexity of O(N) and space complexity O(N)
#
#

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):

        if len(self.items) == 0:
            return None

        popped_value = self.items.pop()

        return popped_value

class Solution:
    def solve (S):
        # write your code in Python 3.6
        stack = Stack()
        #   1. for each element
        for bracket in S:

            if bracket not in {'(', '[', '{', ')', ']', '}'}:
                return 0

            #   2. if element is left handed bracket, push to stack
            if bracket in {'(', '[', '{'}:
                stack.push(bracket)
            #   3. if element is right handed bracket, pop the element
            else:
                popped_bracket = stack.pop()

                #       3.1 if the popped element is not the opposite pair of the right handed bracket, return 0
                if ((bracket == ')' and popped_bracket == '(') or
                    (bracket == ']' and popped_bracket == '[') or
                    (bracket == '}' and popped_bracket == '{')):
                    continue

                return 0

        if len(stack.items) != 0:
            return 0
        #   4. otherwise, return 1
        return 1


if __name__ == '__main__':
    case_1 = "([)()]"
    case_2 = "{[()()]}"
    case_3 = "]["
    case_4 = "[]{}[]{}"
    case_5 = ""
    case_6 = "I (Love) you!["

    expected_1 = 0
    expected_2 = 1
    expected_3 = 0
    expected_4 = 1
    expected_5 = 1
    expected_6 = 0

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