# Brackets
#
# given a string S, consisting of brackets of type '{}', '[]' and '()', create
# an algorithm that determines if brackets in string S is "properly nested".
#
# {[()()]}
#   - a bracket is properly nested if a bracket has a valid matching pair
#
# ([)()]
#   - all brackets has to have a matching pair in another bracket
#
#       ([)()] --> not valid
#       ([])[()] --> is is valid
#
#
#
# input
#   - string
# output
#   - integer
#
# constraints / knowns
#   - the size of string is between [0 ... 200,000]
#   - string only contains the brackets {} and [] and ()
#   - there may be incomplete pair of brackets
#   - use stack to validate the brackets **
#
#   - if solution doesn't exist / invalid, return 0
#   - if string is empty, return 1
#   - if solution exist, return 1

# cases
#   1. if len(S) == 0 --> return 1
#   2. if len(S) == 1 --> return 0
#   3. if len(S) != 1
#
#
# Example
# ([)
# x
# ([]) [(]
# x
#
# ([]) [(,[]
#  x
#
# ([]) [(,[] --> pop element and compare with the current (i.e is current_bracket ')' and if so, popped_bracket = '()')? --> yes
#   x
#
# ([]) [(] --> pop element and compare with the current (i.e is current_bracket ')' and if so, popped_bracket = '()')? --> yes
#    x
#
# return 1
#
# ([) [(]
# x
#
# ([) [(,[]
#  x
#
# ([) [(,[] -->  pop element and compare with the current (i.e is current_bracket ')' and if so, popped_bracket = '()')? --> no ( ')' != '[') --> return 0
#   x
#
#
# ([{) invalid
#
# ()[ [[] --> is size of stack zero -->  no --> return 0
#    x
#
#
# pseudocode
#   1. for each bracket in string
#   2. if bracket is one of ( or [ or {, push the bracket to stack
#   3. if bracket is one of ) or ] or }, pop the bracket from stack and compare
#       3.1 if bracket is ) and popped value is not (, return 0
#       3.2 if bracket is ] and popped value is not [, return 0
#       3.3 if bracket is } and popped value is not {, return 0
#   4. if size of stack is not zero, return 0
#   5. return 1
#
# Time complexity O(N) spatial complexity O(N)


#

class Stack:
    def __init__(self):
        self.items =[]

    def pop(self):

        if len(self.items) == 0:
            return None

        popped_value = self.items.pop()

        return popped_value

    def push(self, value):
        self.items.append(value)


class Solution:
    def solve(self, S):
        stack = Stack()
        #   1. for each bracket in string
        for bracket in S:
            #   2. if bracket is one of ( or [ or {, push the bracket to stack
            if bracket in {'(','[', '{'}:
                stack.push(bracket)
            #   3. if bracket is one of ) or ] or }, pop the bracket from stack and compare
            else:
                popped_bracket = stack.pop()
                #       3.1 if bracket is ) and popped value is not (, return 0
                if ((bracket == ')' and not popped_bracket == '(') or
                    (bracket == ']' and not popped_bracket == '[') or
                    (bracket == '}' and not popped_bracket == '{')):

                    return 0

        #   4. if size of stack is not zero, return 0
        if len(stack.items) != 0:
            return 0

        #   5. return 1
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