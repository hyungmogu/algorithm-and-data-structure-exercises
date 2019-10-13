# Merge Sorted Arrays
#
# In order to win the prize for most cookies sold, my friend Alice and I are
# going to merge our Girl Scout Cookies orders and enter as one unit.
#
#
# Each order is represented by an "order id" (an integer).
#
# We have our lists of orders sorted numerically already, in lists. Write a
# function to merge our lists of orders into one sorted list.
#
# For example:
#
# my_list     = [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print merged_lists(my_list, alices_list)
#
#
# Input
#   list of integers * 2
# Output
#   list of integers
#
# Restriction
#   - the length of two lists are uneven
#   - the two lists are ordered
#
# Example
#
# 1. Here 1 is smaller than 3, so it is put in 'merged_list'
#
# [3, 4, 6, 10, 11, 15]     merged_list = [1]
#  x
#
# [1, 5, 8, 12, 14, 19]
#  ^
#
#
# 2. Here 3 is smaller than 5, so it is put in 'merged_list'
#
# [3, 4, 6, 10, 11, 15]     merged_list = [1,3]
#  x
#
# [1, 5, 8, 12, 14, 19]
#     ^
#
# 3. Here 4 is smaller than 5, so it is put in 'merged_list'
#
# [3, 4, 6, 10, 11, 15]     merged_list = [1,3,4]
#     x
#
# [1, 5, 8, 12, 14, 19]
#     ^
#
# 3. Here 5 is smaller than 6, so it is put in 'merged_list'
#
# [3, 4, 6, 10, 11, 15]     merged_list = [1,3,5]
#        x
#
# [1, 5, 8, 12, 14, 19]
#     ^
#
# [3, 4, 6, 10, 11, 15]     merged_list = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15]
#                       x
# [1, 5, 8, 12, 14, 19]
#                    ^
#
# Pseudocode
#     index_i = 0
#     index_j = 0
#     my_list = []

# #   1. while index_i < len(my_list) and index_j < len(alice_list)
#     while index_i < len(my_list) and index_j < len(alice_list):
#         #   2. if my_list[index_i] <= alice_list[index_j], append my_list[index_i] to merged_list
#         if my_list[index_i] <= alice_list[index_j]:

#             #   2.1 increment the value of index_i
#             #   2.2 continue
#             merged_list.append(my_list[index_i])
#             index_i += 1
#             continue

#         #   3. if my_list[index_i] > alice_list[index_j], append alice_list[index_j] to merged_list
#         #   3.1 increment the value of index_j
#         #   3.2 continue
#         if my_list[index_i] > alice_list[index_j]:
#             merged_list.append(alice_list[index_j])
#             index_j += 1

#     #   4. if index_i < len(my_list), append the rest of element to merged_list
#     if index_i < len(my_list):
#         while index_i < len(my_list):
#             merged_list.append(my_list[index_i])
#             index_i += 1

#     #   5. if index_j < len(alice_list), append the rest of element to merged_list
#     if index_j < len(alice_list):
#         while index_j < len(alice_list):
#             merged_list.append(alice_list[index_J])
#             index_j += 1

#     return merged_list
#
#   6. return merged_list
#
# Time complexity O(M) where M is the size of bigger element, and spatial complexity O(1)
#
#
# The above process is repeated until one reaches the end of alist
# when reached, the index of the bigger array places the remaining elements to the merged list

class Solution:
    def mergeSortedArrays(self, my_list, alice_list):
        index_i = 0
        index_j = 0
        merged_list = []

        #   1. while index_i < len(my_list) and index_j < len(alice_list)
        while index_i < len(my_list) and index_j < len(alice_list):
            #   2. if my_list[index_i] <= alice_list[index_j], append my_list[index_i] to merged_list
            if my_list[index_i] <= alice_list[index_j]:

                #   2.1 increment the value of index_i
                #   2.2 continue
                merged_list.append(my_list[index_i])
                index_i += 1
                continue

            #   3. if my_list[index_i] > alice_list[index_j], append alice_list[index_j] to merged_list
            #   3.1 increment the value of index_j
            #   3.2 continue
            if my_list[index_i] > alice_list[index_j]:
                merged_list.append(alice_list[index_j])
                index_j += 1

        #   4. if index_i < len(my_list), append the rest of element to merged_list
        if index_i < len(my_list):
            while index_i < len(my_list):
                merged_list.append(my_list[index_i])
                index_i += 1

        #   5. if index_j < len(alice_list), append the rest of element to merged_list
        if index_j < len(alice_list):
            while index_j < len(alice_list):
                merged_list.append(alice_list[index_j])
                index_j += 1

        return merged_list
#

if __name__ == '__main__':
    my_list_1 = [3, 4, 6, 10, 11, 15]
    alices_list_1 = [1, 5, 8, 12, 14, 19]

    my_list_2 = []
    alices_list_2 = [1, 5, 8, 12, 14, 19]

    my_list_3 = []
    alices_list_3 = []

    expected_1 = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    expected_2 = [1, 5, 8, 12, 14, 19]
    expected_3 = []

    solution_1 = Solution().mergeSortedArrays(my_list_1, alices_list_1)
    solution_2 = Solution().mergeSortedArrays(my_list_2, alices_list_2)
    solution_3 = Solution().mergeSortedArrays(my_list_3, alices_list_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3