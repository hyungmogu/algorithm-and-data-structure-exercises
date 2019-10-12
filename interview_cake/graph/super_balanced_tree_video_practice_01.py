# Super balanced tree
#
# Write a function to see if a binary tree is "superbalanced"
# (a new tree property we just made up).
#
# This is NOT superbalanced
#
#        10
#      /    \
#     3      4
#    / \
#   6   2
#  /
# 12
#
# This is superbalanced
#
#        10
#      /    \
#     3      4
#    / \
#   6   2
#
#
# A tree is "superbalanced" if the difference between the depths of any two leaf
# nodes is no greater than one.
#
#
#
#        10
#      /    \    current_depth =  2     ->
#     3      4   max_depth = None           max_depth = 2
#    / \         min_depth = None           min_dpeth = 2
#   6   2
#   x
#
#
#        10
#      /    \    current_depth =  1
#  x  3      4
#    / \
#   6   2
#
#
#        10
#      /    \    current_depth =  2
#     3      4   max_depth = 2
#    / \         min_depth = 2
#   6   2
#
#        10
#      /    \
#  x  3      4 current_depth =  1
#    / \
#   6   2
#
#         x
#        10
#      /    \
#     3      4 current_depth =  0
#    / \
#   6   2
#
#
#        10
#      /    \
#     3      4  current_depth =  1  -->
#    / \     x  max_depth = 2               max_depth = 2
#   6   2       min_depth = 2               min_depth = 1
#
#
# max_depth - min_depth = 1 --> superbalalcned --> return True
#
#
# Pseudocode


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
    def __init__(self):
        self.max_depth = None
        self.min_depth = None
        self.current_depth = 0

    def superBlanacedTree(self, root):
        #   1. get maximum and minimum depth of tree using 'getMaxMinDepth'
        self.getMaxMinDepth(root)

        #   2. if max_depth - min_depth > 1, return False
        if self.max_depth - self.min_depth > 1:
            return False
        #   3. else, return True
        return True

    def getMaxMinDepth(self, node):
        # 1. if at leaf node, update max_depth and min_depth
        if node == None:
            if self.max_depth == None or self.current_depth > self.max_depth:
                self.max_depth = self.current_depth

            if self.min_depth == None or self.current_depth < self.min_depth:
                self.min_depth = self.current_depth

            return

        # 2. increase current depth by 1
        # 3. travel recursively using DFS to left and right node of tree
        # 4. decrease current depth by 1
        self.current_depth += 1

        self.getMaxMinDepth(node.left)
        self.getMaxMinDepth(node.right)

        self.current_depth -= 1


if __name__ == '__main__':
    root_case_1 = BinaryTreeNode(10)
    root_case_1.insert_left(3)
    root_case_1.insert_right(2)

    root_case_1.left.insert_left(5)
    root_case_1.left.insert_right(6)

    root_case_1.left.left.insert_left(1)

    root_case_2 = BinaryTreeNode(1)

    root_case_3 = BinaryTreeNode(3)
    root_case_3.insert_left(4)
    root_case_3.insert_right(5)

    root_case_3.left.insert_left(10)

    expected_1 = False
    expected_2 = True
    expected_3 = True

    solution_1 = Solution().superBlanacedTree(root_case_1)
    solution_2 = Solution().superBlanacedTree(root_case_2)
    solution_3 = Solution().superBlanacedTree(root_case_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
