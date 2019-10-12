# Super balanced tree
#
# Write a function to see if a binary tree is "superbalanced"
# (a new tree property we just made up).
#
# A tree is "superbalanced" if the difference between the depths of any two leaf
# nodes is no greater than one.
#
# Solution - using depth first search

# from __init__
    # self.max_depth = 0
    # self.min_depth = 0
    # self.current_depth = 0

#   1. get maximum and minimum depth of tree
#   2. compare the two and see if the difference is greater than 1
#   3. if so, return false
#   4. else return true


# getMaxMinDepth

#   1. for each recursive call, increase depth_count by 1
#   2. if reached the leaf (the end of graph), compare value with the minimum and the maximum depth
    # if node == None
    #     if self.current_depth > self.max_depth:
    #         self.max_depth = self.current_depth
    #     elif self.current_depth < self.min_depth:
    #         self.min_depth = self.current_depth
    #     return

    # self.current_depth += 1

    # self.superBlanacedTree(node.left)

    # self.current_depth -= 1

    # self.superBlanacedTree(node.right)

    # self.current_depth -= 1

#   2.1. if depth greater than minimum, replace minimum with the dpeth value
#   2.2 if depth greater than maximum, replace maximum with the depth value

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
        self.getMaxMinDepth(root)

        if self.max_depth - self.min_depth > 1:
            return False

        return True

    def getMaxMinDepth(self, node):
        if node == None:
            if self.max_depth == None or self.current_depth > self.max_depth:
                self.max_depth = self.current_depth

            if self.min_depth == None or self.current_depth < self.min_depth:
                self.min_depth = self.current_depth
            return

        self.current_depth += 1

        self.superBlanacedTree(node.left)

        self.superBlanacedTree(node.right)

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
