# Binary Search Tree Checker
#
# Write a function to check that a binary tree is a valid binary search tree.
#

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Solution:
    def binarySearchTreeChecker(self, root):
        val_list = []

        self.collectInOrder(root, val_list)

        for index in range (1, len(val_list)):
            if val_list[index - 1] > val_list[index]:
                return False

        return True

    def collectInOrder(self, node, val_list):
        if node:
            self.collectInOrder(node.left, val_list)

            val_list.append(node.val)

            self.collectInOrder(node.right, val_list)

if __name__ == '__main__':
    case_1 = Node(4)
    case_1.left = Node(2)
    case_1.right = Node(5)
    case_1.left.left = Node(1)
    case_1.left.right = Node(3)

    expected = True

    solution = Solution().binarySearchTreeChecker(case_1)

    assert solution == expected