# Largest Smaller BST Key
#
# Given a BST, and a number num, design an efficient algorithm of a method findLargestSmallerKey
# that will return a number that is largest smallest of num. if the solution does not exist,
# return -1.
#
# input
#   - intger, num
#
# output
#   - integer
#
# constraint
#   - if the number doesn't exist, then return -1
#   - all values in bst are positive values
#
#
#          20
#         /   \
#       9      25
#     /   \
#    5      12
#          /  \
#       11     14
#
#
# Example 1
#   num = 17 --> answer = 14
#
# Example 2
#   num = 25 --> answer = 20
#
# Example 3
#   num = 4 --> answer = -1
#
# Example 4
#   num = 10 --> answer = 9
#
# Pseudocode
# def find_largest_smaller_key(self, num):
#     arr = []
#     #   1. using DFS's in-order traversal, put all elements in arr
#     self.collect_elements_in_order(arr, self.root)
#     largest_smaller_key = -1


#     #   2. if arr[0] > num, return -1
#     if arr[0] > num:
#         return largest_smaller_key

#     #   3. for element in arr,
#     for element in arr:
#         #       3.1 if element < num, set largest_smaller_key = element
#         #       3.2 if element > num, return largest_smaller_key
#         if element > num:
#             return largest_smaller_key
#         largest_smaller_key = element

#     #   4. return largest_smaller_key
#     return largest_smaller_key

# def collect_elements_in_order(self, arr, node):

#     if node == None:
#         return

#     self.collect_elements_in_order(arr, node.left)

#     arr.append(node.key)

#     self.collect_elements_in_order(arr, node.right)


#
#
# Tiem complexity O(N), spatial complexity O(N)

class Node:

# Constructor to create a new node
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None

# A binary search tree
class BinarySearchTree:

    # Constructor to create a new BST
    def __init__(self):
        self.root = None

    def find_largest_smaller_key(self, num):
        arr = []
        #   1. using DFS's in-order traversal, put all elements in arr
        self.collect_elements_in_order(arr, self.root)
        largest_smaller_key = -1


        #   2. if arr[0] > num, return -1
        if arr[0] > num:
            return largest_smaller_key

        #   3. for element in arr,
        for element in arr:
            #       3.1 if element < num, set largest_smaller_key = element
            #       3.2 if element > num, return largest_smaller_key
            if element < num:
                largest_smaller_key = element

        #   4. return largest_smaller_key
        return largest_smaller_key

    def collect_elements_in_order(self, arr, node):

        if node == None:
            return

        self.collect_elements_in_order(arr, node.left)

        arr.append(node.key)

        self.collect_elements_in_order(arr, node.right)

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):
        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)

        while(currentNode is not None):
            if(key < currentNode.key):
                if(currentNode.left is None):
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if(currentNode.right is None):
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right

#########################################
# Driver program to test above function #
#########################################

bst  = BinarySearchTree()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

result = bst.find_largest_smaller_key(10)

print ("Largest smaller number is %d " %(result))
