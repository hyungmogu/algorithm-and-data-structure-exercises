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


#============= solution ==============

class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):

        if len(self.items) == 0:
            return None

        return self.items.pop()


def solution(S):
    # write your code in Python 3.6
    brackets_stack = Stack()
    lhs_brackets_list = ['(', '[', '{']
    rhs_brackets_list = [')', ']', '}']

    for bracket in S:
        # if left hand brackets, push to stack
        if bracket in lhs_brackets_list:
            brackets_stack.push(bracket)

        # if right hand elements, pop stack and compare
        if bracket in rhs_brackets_list:
            lhs_bracket = brackets_stack.pop()

            # if not matching, then return 0
            if ((bracket == ')' and lhs_bracket != '(') or
                (bracket == ']' and lhs_bracket != '[') or
                (bracket == '}' and lhs_bracket != '{')):
                return 0

    # if length of stack is non-zero, then return 0
    if len(brackets_stack.items) != 0:
        return 0

    # otherwise return 1
    return 1
