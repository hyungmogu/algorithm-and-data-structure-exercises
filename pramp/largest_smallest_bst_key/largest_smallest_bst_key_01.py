# Largest Smaller BST Key
# Given a root of a Binary Search Tree (BST) and a number num, implement an efficient
# function findLargestSmallerKey that finds the largest key in the tree that is smaller
# than num. If such a number doesn't exist, return -1. Assume that all keys in the
# tree are nonnegative.
#
# Analyze the time and space complexities of your solution.
#
# For example:
#
# For num = 17 and the binary search tree below:
#
# alt
#
# Your function would return:
#
# 14 since it's the largest key in the tree that is still smaller than 17.
#
# Constraints:
#
# [time limit] 5000ms
# [input] Node rootNode
# [output] integer
#
#          20
#         /   \
#       9      25
#     /   \
#    5      12
#          /  \
#       11     14
#

##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################
#
#
# PSEUDOCODE
# 1. using in-order depth first search, store all elements in array 'arr'
# 2. if arr[0] > num, return -1
# 3. for each element in array, if element < number, then return set largest_smallest_key = element
# 4. return element

# Time complexity of O(N) and spatial complexity of O(N)
# A node
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
    # Write solution here
    # PSEUDOCODE
    arr = []

    # 1. using in-order depth first search, store all elements in array 'arr'
    self.get_all_elements(arr, self.root)

    # 2. if arr[0] > num, return -1
    if arr[0] > num:
      return -1

    # 3. for each element in array, if element < number, then return set largest_smallest_key = element
    largest_smaller_key = arr[0]

    for element in arr:
      if element < num:
        largest_smaller_key = element

    return largest_smaller_key

  def get_all_elements(self, arr, node):

    if node == None:
      return

    self.get_all_elements(arr, node.left)

    arr.append(node.key)

    self.get_all_elements(arr, node.right)






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

result = bst.find_largest_smaller_key(11)

print ("Largest smaller number is %d " %(result))
