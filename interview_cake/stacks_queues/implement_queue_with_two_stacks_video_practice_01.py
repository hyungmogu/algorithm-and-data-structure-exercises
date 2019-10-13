# Implement Queue with Two Stacks
#
# Implement a queue with 2 stacks. Your queue should have an enqueue and a
# dequeue method and it should be "first in first out" (FIFO).
#
#
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

#           |
#           3       Last
#           |
#           2
#           |
#           1       First
#       _________

# 1. Enqueue operation
#   1. push item to stack1
#     self.stack1.push(val)

# # 2. Dequeue operation


# #           |
# #           3       Last
# #           |
# #           2
# #           |
# #           1       First
# #       _________  stack 1




# #           |
# #           |
# #           |
# #       _________ stack1

# #           |
# #           1
# #           |
# #           2
# #           |
# #           3
# #       _________ stack2


# #  first_item = 1

# #           |
# #           |
# #           |
# #       _________ stack2

# #           |
# #           |
# #           3
# #           |
# #           2
# #       _________ stack1


# # 1. pop all elements from stack 1 and put in stack 2
#     at_end_12 = False
#     at_end_21 = False

#     while not at_end_12:
#         popped_element = self.stack1.pop()

#         # 2. pop last element from stack 2 and save in 'first_item'
#         if popped_element == None:
#             first_item = self.stack2.pop()
#             at_end_12 = True
#             continue

#         self.stack2.push(popped_element)


#     # 3. pop all elements from stack 2 and put in stack 1

#     while not at_end_21:
#         popped_element = self.stack2.pop()

#         if popped_element == None:
#             at_end_21 = True
#             continue

#         self.stack1.push(popped_element)



# # 4. return the first_item
#     return first_item


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
        # 1. pop all elements from stack 1 and put in stack 2
        at_end_12 = False
        at_end_21 = False

        while not at_end_12:
            popped_element = self.stack1.pop()

            # 2. pop last element from stack 2 and save in 'first_item'
            if popped_element == None:
                first_item = self.stack2.pop()
                at_end_12 = True
                continue

            self.stack2.push(popped_element)


        # 3. pop all elements from stack 2 and put in stack 1

        while not at_end_21:
            popped_element = self.stack2.pop()

            if popped_element == None:
                at_end_21 = True
                continue

            self.stack1.push(popped_element)

        # 4. return the first_item
        return first_item



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


