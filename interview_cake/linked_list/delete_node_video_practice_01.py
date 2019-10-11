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
# Example
# A   ->    B    ->   C
#
# Head and prev node inaccessible --> How can we remove node 'B' and have link list of form 'A - C'?
#
# New Solution

# Time complexity O(1) and spatial complexity O(1)
#
#
# case
# A -> B ?

def delete_node(node):
    if node.next == None:
        del node
        return

    #   1. given node, set node.value = node.next.value
    node.value = node.next.value
    #   2. given node, set node.next = node.next.next
    node.next = node.next.next


if __name__ == '__main__':
    case_1a = LinkedListNode('A')
    case_1b = LinkedListNode('B')
    case_1c = LinkedListNode('C')

    case_1a.next = case_1b
    case_1b.next = case_1c

    delete_node(case_1b)

    assert case_1a.next.value == 'C'
    assert case_1b.next == None

    case_2a = LinkedListNode('A')
    case_2b = LinkedListNode('B')

    delete_node(case_2b)
    assert case_2a.next == None