# Reverse Linked List
#
# Hooray! It's opposite day. Linked lists go the opposite way today.
#
# Write a function for reversing a linked list. Do it in place.
#
# Your function will have one input: the head of the list.
#
# Your function should return the new head of the list.
#
# Here's a sample linked list node class:

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next  = None

# Input
#   - linkedListNode (head / root)
# Output
#   - linkedListNode (new head/root)

# Example
#                           v
#   1 --> 2 --> 3 --> 4 --> 5
#
#
#     Tail: {5}
#     Head: {1}
# New Head: {5}
#
#
#                           *     v
#   1 --> 2 --> 3 --> 4 --> 5 --> 4
#
#
#     Tail: {4}
#     Head: {1}
# New Head: {5}
#
#                           *           v
#   1 --> 2 --> 3 --> 4     5 --> 4 --> 3
#
#
#     Tail: {3}
#     Head: {1}
# New Head: {5}
#
#
#                           *                 v
#   1 --> 2 --> 3           5 --> 4 --> 3 --> 2
#
#
#     Tail: {2}
#     Head: {1}
# New Head: {5}
#
#
#                           *                       v
#   1 --> 2                 5 --> 4 --> 3 --> 2 --> 1
#
#
#     Tail: {1}
#     Head: {1}
# New Head: {5}
#
#
#                           *                       v
#                           5 --> 4 --> 3 --> 2 --> 1 --> None
#
#
#     Tail: {1}
#     Head: {1}
# New Head: {5}
#
#
# Brute Force Solutions

def __init__(self):
    self.tail = None
    self.head = None
    self.new_head = None

def reverseLinkedList(self, root):
    self.head = root

    self.getReversedLinkedList(root)

    return self.new_head

def getReversedLinkedList(self, node):
    #   1. if at the end of linked list by the end of recursive travel (node.next == None <-- this is the base case)
    #   1.1. set self.tail = node and self.new_head = node

    if node.next == None:
        self.tail = node
        self.new_head = node
        return

    #   2. Recursively travel until the end of linked list (getRecursiveLinkedList(node.next))
    self.getReversedLinkedList(node.next)

    #   3. Set self.tail.next = node and self.tail = node
    self.tail.next = node
    self.tail = node

    #   4. if self.head == self.tail
    #   4.1 set self.tail.next = None
    if self.head == self.tail:
        self.tail.next = None
        #   5. retrun 'self.new_head'


class Solution:
    def __init__(self):
        self.tail = None
        self.head = None
        self.new_head = None

    def reverseLinkedList(self, root):
        self.head = root

        self.getReversedLinkedList(root)

        return self.new_head

    def getReversedLinkedList(self, node):
        #   1. if at the end of linked list by the end of recursive travel (node.next == None <-- this is the base case)
        #   1.1. set self.tail = node and self.new_head = node

        if node.next == None:
            self.tail = node
            self.new_head = node
            return

        #   2. Recursively travel until the end of linked list (getRecursiveLinkedList(node.next))
        self.getReversedLinkedList(node.next)

        #   3. Set self.tail.next = node and self.tail = node
        self.tail.next = node
        self.tail = node

        #   4. if self.head == self.tail
        #   4.1 set self.tail.next = None
        if self.head == self.tail:
            self.tail.next = None
            #   5. retrun 'self.new_head'

if __name__ == '__main__':
    case_1 = LinkedListNode(1)
    case_1.next = LinkedListNode(2)
    case_1.next.next = LinkedListNode(3)
    case_1.next.next.next = LinkedListNode(4)
    case_1.next.next.next.next = LinkedListNode(5)

    expected_1_1 = 5
    expected_1_2 = 4
    expected_1_3 = 3
    expected_1_4 = 2
    expected_1_5 = 1

    solution_1_1 = Solution().reverseLinkedList(case_1)
    solution_1_2 = solution_1_1.next
    solution_1_3 = solution_1_1.next.next
    solution_1_4 = solution_1_1.next.next.next
    solution_1_5 = solution_1_1.next.next.next.next

    assert expected_1_1 == solution_1_1.value
    assert expected_1_2 == solution_1_2.value
    assert expected_1_3 == solution_1_3.value
    assert expected_1_4 == solution_1_4.value
    assert expected_1_5 == solution_1_5.value