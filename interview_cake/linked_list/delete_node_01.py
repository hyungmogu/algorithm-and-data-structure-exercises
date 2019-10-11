# Delete Node
# Given Linked List Node

class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

# Create an algorithm that deletes a node by variable
# The input could, for example, be the variable b below:
#
# a = LinkedListNode('A')
# b = LinkedListNode('B')
# c = LinkedListNode('C')
#
# a.next = b
# b.next = c
#
# delete_node(b)
#
# Input
#   - LinkListNode
#
# Output
#   - None
#
# Example
#
#
# A  -   B  -   C
#
# A  -   B  -   C
# ^     DELETE
# |
# a.next = c
#
#
# A - C
#
# First Thought
#   1. before the end, traverse through the linked list
#   2. if the next node is the same as the variable, then remove the node
#   3. return None


# BUT WAIT!!!! We can't access the previous node. How can we delete node if we cant access it?
#
#
# New Solution
#   1. Set the value of B the same as C
#   2. set b.next (now c) to None

def delete_node(node):

    if node.next == None:
        return # This is incorrect. This doesn't consider the case delete_node(b) in 'A - B'

    node.value = node.next.value
    node.next = None # This is incorrect. should be node.next.next.

if __name__ == '__main__':
    a = LinkedListNode('A')
    b = LinkedListNode('B')
    c = LinkedListNode('C')

    a.next = b
    b.next = c

    delete_node(b)

    assert a.next.value == 'C'
    assert b.next == None