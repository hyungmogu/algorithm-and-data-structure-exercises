# 2nd largest item in BST
#
# Write a function to find the 2nd largest element in a binary search tree
# given the following binary search tree class
#
# Brute force solution
def inOrderTraversal(self, node, arr):
#   1. Using in-order Depth first search, collect all values in an array
    if node == None:
        return

    self.inOrderTraversal(node.left, arr)

    arr.append(node.value)

    self.inOrderTraversal(node.right, arr)


def secondLargestItem(self, root):
    arr = []

    self.inOrderTraversal(root, arr)

    #   2. if len(arr) > 1, return arr[-2]
    #   3. if len(arr) <= 1, return None
    if len(arr) <= 1:
        return None

    return arr[-2]

# This has O(N) time complexity and O(N) spatial complexity --> O(N) here the
# time complexity is due to call stack and collection of values

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


class Solution:
    def secondLargestItem(self, root):
        arr = []

        self.inOrderTraversal(root, arr)

        #   2. if len(arr) > 1, return arr[-2]
        #   3. if len(arr) <= 1, return None
        if len(arr) <= 1:
            return None

        return arr[-2]

    def inOrderTraversal(self, node, arr):
        #   1. Using in-order Depth first search, collect all values in an array
        if node == None:
            return

        self.inOrderTraversal(node.left, arr)

        arr.append(node.value)

        self.inOrderTraversal(node.right, arr)


if __name__ == '__main__':
    case_1 = BinaryTreeNode(4)
    case_1.left = BinaryTreeNode(2)
    case_1.right = BinaryTreeNode(5)
    case_1.left.left = BinaryTreeNode(1)
    case_1.left.right = BinaryTreeNode(3)

    case_2 = BinaryTreeNode(10)
    case_2.left = BinaryTreeNode(5)
    case_2.right = BinaryTreeNode(12)
    case_2.left.left = BinaryTreeNode(4)
    case_2.left.right = BinaryTreeNode(7)

    expected_1 = 4
    expected_2 = 10

    solution_1 = Solution().secondLargestItem(case_1)
    solution_2 = Solution().secondLargestItem(case_2)

    assert solution_1 == expected_1
    assert solution_2 == expected_2