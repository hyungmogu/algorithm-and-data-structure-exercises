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

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# input
#   - list of integers
#
# output
#   - integers (return 1 if S properly nested 0 otherwise)
#
# constraint
#   - N is an integer within the range [0 ... 200,000]
#   - S consists of the following characters '(', '{' and '['
#
# Example
# A = '([{()()}])' --> all valid
# A = '(([{)()}])' --> invalid
# A = '([{()()}])' --> invalid
# A = '([({' -> invalid

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):

        if len(self.items) == 0:
            return None

        return self.items.pop()

def solution(S):
    # 1. for each left braket in A, store inside stack array
    stack = Stack()

    for bracket in S:
        if ((bracket == '(') or
            (bracket == '[') or
            (bracket == '{')):

            stack.push(bracket)
            continue

        popped_bracket = stack.pop()

        # 2. for each right bracket in A, pop the array and compare
        #   2.1 if not the corresponding array, then return value 0
        if ((bracket == ')' and not popped_bracket == '(') or
            (bracket == ']' and not popped_bracket == '[') or
            (bracket == '}' and not popped_bracket == '{')):

            return 0

    # 3. if the length of stack is non-zero return 0
    if len(stack.items) != 0:
        return 0

    return 1
    # 4. return 1

