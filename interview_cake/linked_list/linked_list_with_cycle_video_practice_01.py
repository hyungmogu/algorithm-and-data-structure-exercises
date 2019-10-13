# Does this Linked List have a cycle?
#
# You have a singly-linked list and want to check if it contains a cycle.
#
# A singly-linked list is built with nodes, where each node has:
#
# - node.next—the next node in the list.
# - node.value—the data held in the node. For example, if our linked list stores
#   people in line at the movies, node.value might be the person's name.
#
#
# For example:
#
# For example:

class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

# A cycle occurs when a node’s next points back to a previous node in the list.
# The linked list is no longer linear with a beginning and end—instead, it cycles
# through a loop of nodes.
#
# Write a function contains_cycle() that takes the first node in a singly-linked
# list and returns a boolean indicating whether the list contains a cycle.
#
#
#     10   -   11    -   5
#                     /       \
#                    6         2
#                     \       /
#                       4 -  3
#
#
# Solution
#     second_pointer = node
#     first_pointer = node

# #   1. while second pointer has not met the first pointer
#     while not second_pointer.next == first_pointer:
#         #   2.1 increment second pointer by 2 elements

#         #   2.2 increment first pointer by 1 element
#         #   3. if second pointer is None, return False
#         #   4. if second pointer throws error, return False
#         try:
#             second_pointer = second_pointer.next.next
#             first_pointer =first_pointer.next

#             if second_pointer == None:
#                 return False
#         except Exception:
#             return False

#     return True

#   5. return True
class Solution:
    def contains_cycle(self, node):
        second_pointer = node
        first_pointer = node

        # 1. while second pointer has not met the first pointer
        while not second_pointer.next == first_pointer:
            #   2.1 increment second pointer by 2 elements
            #   2.2 increment first pointer by 1 element
            #   3. if second pointer is None, return False
            #   4. if second pointer throws error, return False
            try:
                second_pointer = second_pointer.next.next
                first_pointer =first_pointer.next

                if second_pointer == None:
                    return False
            except Exception:
                return False

        return True


if __name__ == '__main__':
    node_1_case_1 = LinkedListNode(10)
    node_2_case_1 = LinkedListNode(11)
    node_3_case_1 = LinkedListNode(5)
    node_4_case_1 = LinkedListNode(3)
    node_5_case_1 = LinkedListNode(4)
    node_6_case_1 = LinkedListNode(6)

    node_1_case_1.next = node_2_case_1
    node_2_case_1.next = node_3_case_1
    node_3_case_1.next = node_4_case_1
    node_4_case_1.next = node_5_case_1
    node_5_case_1.next = node_6_case_1
    node_6_case_1.next = node_3_case_1

    expected_1 = True
    solution_1 = Solution().contains_cycle(node_1_case_1)

    assert expected_1 == solution_1

    node_1_case_2 = LinkedListNode(1)
    node_2_case_2 = LinkedListNode(2)
    node_3_case_2 = LinkedListNode(3)
    node_4_case_2 = LinkedListNode(4)

    node_1_case_1.next = node_2_case_2
    node_2_case_1.next = node_3_case_2
    node_3_case_1.next = node_4_case_2

    expected_2 = False
    solution_2 = Solution().contains_cycle(node_2_case_1)

    assert expected_2 == solution_2
