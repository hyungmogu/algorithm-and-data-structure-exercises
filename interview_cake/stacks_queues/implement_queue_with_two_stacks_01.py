# Implement Queue with Two Stacks
#
# Implement a queue with 2 stacks. Your queue should have an enqueue and a
# dequeue method and it should be "first in first out" (FIFO).
#
#
# Here, we have to throughly understand both stack and queue to solve this problem
#   - stack is LIFO (LAST IN FIRST OUT)
#   - Example: List
#
#           |
#           3       Last
#           |
#           2
#           |
#           1       First
#       _________
#
#   - Queue is FIFO (FIRST IN FIRST OUT)
#   - has operations dequeue and enqueue
#   - dequeue --> takes out the first added item from the data structure
#   - enqueue --> places an element into data structure
#
#       3   -   2   -   1
#     Last             First
#

# 1. pop
#   1. if self.items is emoty, then None is returned
#   2. if self.items is not empty, then pop element from self.items and return the popped element

# 2. push
#   1. append element into self.items
#
#
# Queue
#   1. enqueue
#       - push elements to stack1
# #         self.stack1.push(val)
# #   2. dequeue
# #       - pop all elements from stack1 and push to stack2
# #       - if popped element is last then save the element
#             at_end_12 = False
#             first_element = None

#             while not at_end_12
#                 popped_element = stack1.pop()

#                 if popped_element == None:
#                     at_end = True
#                     continue

#                 first_element = popped_element
#                 stack2.push(popped_element)

#             return first_element


# #       - pop all elements from stack2 and push to stack 1

#             at_end_21 = False
#             while not at_end_12
#                 popped_element = stack2.pop()

#                 if popped_element == None:
#                     at_end = True
#                     continue

#                 stack1.push(popped_element)

# both enqueue and dequeue has time complexity of O(N) and spatial complexity of ON)




class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if len(self.items) == 0:
            return None

        popped_element = self.items.pop()

        return popped_element


class Solution:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, val):
        self.stack1.push(val)

    def dequeue(self):
        at_end_12 = False
        first_element = None

        while not at_end_12:
            popped_element = self.stack1.pop()

            if popped_element == None:
                first_element = self.stack2.pop()
                at_end_12 = True
                continue

            self.stack2.push(popped_element)

        #  - pop all elements from stack2 and push to stack 1
        at_end_21 = False
        while not at_end_21:
            popped_element = self.stack2.pop()

            if popped_element == None:
                at_end_21 = True
                continue

            self.stack1.push(popped_element)

        return first_element


if __name__ == '__main__':
    case_1 = Solution()
    case_1.enqueue(1)
    case_1.enqueue(2)
    case_1.enqueue(3)

    expected_1 = [1, 2, 3]

    solution_1 = case_1.stack1.items

    print(solution_1)

    assert expected_1 == solution_1


    case_2 = Solution()
    case_2.stack1.items = [1, 2, 3]

    case_2.dequeue()

    expected_2 = [2, 3]
    solution_2 = case_2.stack1.items

    assert expected_2 == solution_2

    case_2.dequeue()

    expected_2 = [3]
    solution_2 = case_2.stack1.items

    assert expected_2 == solution_2

    case_2.dequeue()

    expected_2 = []
    solution_2 = case_2.stack1.items

    assert expected_2 == solution_2


