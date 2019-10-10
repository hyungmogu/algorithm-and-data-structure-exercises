# Binary Search Tree Checker
#
# Write a function to check that a binary tree is a valid binary search tree.
#
#
#       4
#     /   \
#    3     1
#
#
#      2
#    /   \
#   1     5
#
#
#        6
#     /    \
#    4       7
#  /   \
# 1     5
#
#
#     x
# [1, 4, 5, 6, 7]
#
# known
#   - DFS in order --> walks through elements in order
#
# Input
#   - Node
# Output
#   - Boolean
#
# Brute Force Solution

# Time complexity O(N) + O(N) --> O(2N) --> O(N) Spatial complexity O(N)

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class Solution:
    def binarySearchTreeChecker(self, root):
        # 1. using in order traversal DFS algorithm, collect traversed elements into a list 'val_list'
        val_list = []

        if len(val_list) == 1:
            return True

        self.collectValuesInOrder(root, val_list)

        # 2. walk through each element in the list and return false if elements not in order

        for index in range(1, len(val_list)):
            if val_list[index - 1] > val_list[index]:
                return False

        # 3. return True if on order
        return True

    def collectValuesInOrder(self, node, val_list):
        if node:
            self.collectValuesInOrder(node.left, val_list)

            val_list.append(node.value)

            self.collectValuesInOrder(node.right, val_list)



if __name__ == '__main__':
    case_1 = Node(4)
    case_1.left = Node(2)
    case_1.right = Node(5)
    case_1.left.left = Node(1)
    case_1.left.right = Node(3)

    expected = True

    solution = Solution().binarySearchTreeChecker(case_1)

    assert solution == expected