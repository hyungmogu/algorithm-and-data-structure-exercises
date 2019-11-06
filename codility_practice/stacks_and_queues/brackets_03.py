# Brackets
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
#
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

#
# ================ solution ===============
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal:
#   - creating an algorithm that checks if a string is properly nested
#
# known
#   - return 1 if S is properly nested
#   - return 0 otherwise
#
# constraint
#   - N is an integer in range [0 ... 200,000]
#   - String S only contains the following characters "(", "{" and "["
#


# pseudocode
#   1. for each left hand brackets, put it in stack
#   2. for each right hand bracket, pop left hand bracket and compare
#   3. if not matching bracket, then return 0
#   4. if all is well, return 1

# Time Complexity O(N), spatial complexity O(N)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):

        if len(self.items) == 0:
            return None

        popped_value = self.items.pop()

        return popped_value

def solution(S):
    # pseudocode
    stack = Stack()
    #   1. for each left hand brackets, put it in stack
    for bracket in S:
        if bracket in {'{', '[', '('}:
            stack.push(bracket)

        #   2. for each right hand bracket, pop left hand bracket and compare
        #   3. if not matching bracket, then return 0
        if bracket in {'}', ']', ')'}:
            popped_bracket = stack.pop()

            if popped_bracket == None:
                return 0

            if ((bracket == ')' and popped_bracket != '(') or
                (bracket == ']' and popped_bracket != '[') or
                (bracket == '}' and popped_bracket != '{')):
                    return 0

    #   4. if size of items not empty, return 0
    if len(stack.items) != 0:
        return 0

    #   5. if all is well, return 1

    return 1
