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
#   - the two lists are ordered
#
# Solution
#   - We can do this in O(M) time complexity where M represents the bigger of two arrays!!
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
# 2. Here 4 is smaller than 5, so it is put in 'merged_list'
#
# [3, 4, 6, 10, 11, 15]     merged_list = [1,3,4]
#        x
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
# The above process is repeated until one reaches the end of alist
# when reached, the index of the bigger array places the remaining elements to the merged list


# pseudocode
# 1. for pointer i in 'my_list' and for pointer j in 'alicees_list', and while i < len(my_list) and i < len(alices_list)
#     merged_list = []

#     index_i = 0
#     index_j = 0

#     # 2. if my_list[i] >= alices_list[j], then append my_list[i] to 'merged_list '.
#     # 2.1 increment pointer i
#     # 3 if my_list[i] < alices_list[j], then append alices_list[j] to 'merged_list'
#     # 3.1 increment pointer j
#     while index_i < len(my_list) and index_j < len(alices_list):
#         if my_list[index_i] >= alices_list[index_j]:
#             merged_list.append(alices_list[index_j])
#             index_j += 1
#             continue

#         merged_list.append(my_list[index_i])
#         index_i += 1

# #
# # 4. if len(my_list) > len(alices_list), append the remaining elements in my_list to merged_list

#     if len(my_list) > len(alices_list):
#         while index_i < len(my_list):
#             merged_list.append(my_list[index_i])
#             index_i += 1

# # 5. if len(my_list) < len(alices_list), append the remaining elements in alices_list to merged_list

#     if len(my_list) < len(alices_list):
#         while index_j < len(alices_list):
#             merged_list.append(my_list[index_j])
#             index_j += 1

# # 6. return merged_list
#     return merged_list


class Solution:
    def mergeSortedArrays(self, my_list, alices_list):
        # 1. for pointer i in 'my_list' and for pointer j in 'alicees_list', and while i < len(my_list) and i < len(alices_list)
        merged_list = []

        index_i = 0
        index_j = 0

        # 2. if my_list[i] >= alices_list[j], then append my_list[i] to 'merged_list '.
        # 2.1 increment pointer i
        # 3 if my_list[i] < alices_list[j], then append alices_list[j] to 'merged_list'
        # 3.1 increment pointer j
        while index_i < len(my_list) and index_j < len(alices_list):
            if my_list[index_i] >= alices_list[index_j]:
                merged_list.append(alices_list[index_j])
                index_j += 1
                continue

            merged_list.append(my_list[index_i])
            index_i += 1

        # 4. if len(my_list) > len(alices_list), append the remaining elements in my_list to merged_list
        if len(my_list) >= len(alices_list):
            while index_i < len(my_list):
                merged_list.append(my_list[index_i])
                index_i += 1

        # 5. if len(my_list) < len(alices_list), append the remaining elements in alices_list to merged_list
        if len(my_list) <= len(alices_list):
            while index_j < len(alices_list):
                merged_list.append(alices_list[index_j])
                index_j += 1

        # 6. return merged_list
        return merged_list


if __name__ == '__main__':
    my_list_1 = [3, 4, 6, 10, 11, 15]
    alices_list_1 = [1, 5, 8, 12, 14, 19]

    expected_1 = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

    solution_1 = Solution().mergeSortedArrays(my_list_1, alices_list_1)

    assert expected_1 == solution_1