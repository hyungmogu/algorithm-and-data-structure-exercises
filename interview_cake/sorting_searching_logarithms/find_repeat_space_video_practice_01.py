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
# constraint
#   - only one repeat element needs to be returned
#   - there will always be one repeat element
#   - we are priortizing spatial complexity
#
# [1,3,2,1,5] --> 1
# [1,3,2,1,3,4,5] --> 1, 3
#
# [1,3,2,1,5] --> 1
#  x
#        ^
#
# Brute force solution
#   1. for each pointer x in arr
#   2. for each pointer y in arr
#   2.1. if index_x == index_y, continue
#   2.2. if x == y, then return x
#
# time complexity O(N^2) spatial O(1)
#
# YES!!! we can improve the time complexity
#   -> sorting O(N*logN) -> [1,1,2,3,5]
#
#   NOTE!! LIST.sort() --> in-place, sorted() --> NOT in-place
#   Improved solution
# #       1. sort arr
#             index = 1
#             arr.sort()

# #       2. while index = 1, and index < len(arr),
#             while index < len(arr):

# #       2.1 if arr[index] == arr[index-1], return arr[index]
#                 if arr[index] == ar[index-1]:
#                     return arr[index]

#                 index += 1
class Solution:
    def findRepeatSpace(self, arr):
#       1. sort arr
        index = 1
        arr.sort()

#       2. while index = 1, and index < len(arr),
        while index < len(arr):

#       2.1 if arr[index] == arr[index-1], return arr[index]
            if arr[index] == arr[index-1]:
                return arr[index]

            index += 1

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