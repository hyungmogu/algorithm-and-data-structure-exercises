# Largest Element in Stack
#
# Given the stack

class Stack:

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


# Use your Stack class to implement a new class MaxStack with a method get_max()
# that returns the largest element in the stack. get_max() should not remove the item.
#
# Example
#
#  [    ]
#
# Last                                                             First
#
#  max_value = 10
#
#
# [                       5      -     9     -   10   -     2     -    1 ]
#
#  LAST                                                             FIRST
#
# return max_value
#
# O(N) --> O(1)
#
#
# Improved solution
#
#
#
#  1           -        2           -    10          -       9        -     5
#
#
# [ 5, 9,  10, 10]
#
#
class MaxStack(Stack):
    def __init__(self):
        super().__init__()
        self.max_val_list = []

    def push(self, val):
        super().__init__()

        # 0. if 'max_val_list' is empty, append val

        if len(self.max_val_list) == 0:
            self.max_val_list.append(val)
            return

        # 1. if val is current_max in 'max_val_list', append val

        if val > self.max_val_list[-1]:
            self.max_val_list.append(val)
        else:
        # 2. if val is not current_ma in 'max_val_list', append max_val_list[-1]
            self.max_val_list.append(self.max_val_list[-1])


    def pop(self):
        super().pop()
        # 1. pop element from max_val_list

        self.max_val_list.pop()


    def get_max(self):
        return self.max_val_list[-1]

if __name__ == '__main__':
    stack = MaxStack()
    stack.push(5)
    stack.push(9)
    stack.push(10)
    stack.push(2)
    stack.push(1)

    expected_1 = 10
    expected_2 = 10
    expected_3 = 10
    expected_4 = 9
    expected_5 = 5

    solution_1 = stack.get_max()
    stack.pop()

    solution_2 = stack.get_max()
    stack.pop()

    solution_3 = stack.get_max()
    stack.pop()

    solution_4 = stack.get_max()
    stack.pop()

    solution_5 = stack.get_max()
    stack.pop()

    assert solution_1 == expected_1
    assert solution_2 == expected_2
    assert solution_3 == expected_3
    assert solution_4 == expected_4
    assert solution_5 == expected_5

