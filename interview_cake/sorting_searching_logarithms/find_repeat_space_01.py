# Find a duplicate, Space Edition™.
#
# We have a list of integers, where:
#
# The integers are in the range 1..n1..n
# The list has a length of n+1n+1
# It follows that our list has at least one integer which appears at least twice.
# But it may have several duplicates, and each duplicate may appear more than twice.
#
# Write a function which finds an integer that appears more than once in our list.
# (If there are multiple duplicates, you only need to find one of them.)
#
# We're going to run this function on our new, super-hip MacBook Pro With Retina
# Display™. Thing is, the damn thing came with the RAM soldered right to the
# motherboard, so we can't upgrade our RAM. So we need to optimize for space!
#
#   Input
#       - list of integers
#   output
#       - integer
#
#   restriction
#       - need to find one repeat integers
#       - there is at least one repeat integers
#       - priortize spatial complexity!!
#
#   Brute force solution
#   1. for each element in arr,
#   1.1 find repeat element by iterating all other elements except itself
#   1.2 if repeat element found, repeat result
#
#   Here in this case, has O(N^2) time complexity and O(1) spatial complexity
#
#
#   We can do better --> using sorting
#       - python's .sort method is in-place with time complexity of O(N*logN)
#
#   [1,3,2,1,3,4,5]
#
#   [1,1,2,3,3,4,5]
#      x
#   Improved solution
#   1. sort array
#     index = 1
#     sorted_list = arr.sort()

# #   2. for each element starting at index = 1,
#     while index < len(sorted_list):
#         if sorted_list[index - 1] == sorted_list[index]:
#             return arr[index]
# #   3. if arr[index - 1] == arr[index], then return arr[index]

class Solution:
    def findRepeatSpace(self, arr):
        index = 1
        arr.sort()

        #   2. for each element starting at index = 1,
        while index < len(arr):
            if arr[index - 1] == arr[index]:
                return arr[index]

if __name__ == '__main__':
    case_1 = [1,3,2,1,5]
    case_2 = [1,3,2,1,3,4,5]

    expected_1 = 1
    expected_2 = 1

    solution_1 = Solution().findRepeatSpace(case_1)
    solution_2 = Solution().findRepeatSpace(case_2)

    assert expected_1 == solution_1
    assert expected_2 == solution_2