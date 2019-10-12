# Highest Product of 3
#
#
# Given a list of integers, find the highest product you can get from three of
# the integers.
#
# The input list_of_ints will always have at least three integers.
#
# Input
#   - list of integers
# Output
#   - Integer (highest value after multiplying three elements)
#
# Constraint
#   - there can be negative numbers as well as positive
#   - list_of_ints will always have at least three integers.
#
#
#
# Example
# [9, 1, 5, 16, 2, 3] -> 720
#  x
#     ^
#        *
# Brute Force Solution
#   1. using three pointers to find product of three elements that gives the highest number
#
# Time complexity of O(N^3) spatial complexity of O(1)
#
#
#
# !!The better way of solving the problem!!
#
# [third_highest, second_highest, highest]
#
# Example
# [9, 1, 5, 16, 2, 3] -> [None, None, 9]
#  x
#
# [9, 1, 5, 16, 2, 3] -> [None, 1, 9]
#     x
#
# [9, 1, 5, 16, 2, 3] -> [1, 5, 9]
#        x
#
# # [9, 1, 5, 16, 2, 3] -> [5, 9, 16]
#              x
#
# [9, 1, 5, 16, 2, 3] -> [5, 9, 16]
#               x
#
# # [9, 1, 5, 16, 2, 3] -> [5, 9, 16] --> 720
#                    x
#
# Time complexity of O(N) and spatial complexity of O(1)
#
# Example
# [-10,-10, 3, 1, 5, 2] -> [-10, -10] --> 100 * highest_val_list[-1] > total_product
# total_product = 100 * highest_val_list[-1]
# reutnr total_product

import functools

# Example 2
# [-10, -10, 3, 1, 5, 2] -> 500
class Solution:
    def highestProductOf3(self, list_of_ints):
        highest_val_list = [None, None, None]

        #   1. for each element in 'list_of_ints'
        for element in list_of_ints:
            #   1.1 if list_of_ints[2] is None or list_of_ints[2] < element, set list_of_ints[2] = element
            #   1.2 move list_of_ints[2] to list_of_ints[1] and list_of_ints[1] to list_of_ints[0]
            #   1.3 continue
            if highest_val_list[2] is None or highest_val_list[2] < element:
                highest_val_list[0] = highest_val_list[1]
                highest_val_list[1] = highest_val_list[2]
                highest_val_list[2] = element
                continue

            #   2.1 if list_of_ints[1] is None or list_of_ints[1] < element, set list_of_ints[1] = element
            #   2.2 move list_of_ints[1] to list_of_ints[0]
            #   2.3 continue
            if highest_val_list[1] is None or highest_val_list[1] < element:
                highest_val_list[0] = highest_val_list[1]
                highest_val_list[1] = element
                continue

            #   3.1 if list_of_ints[0] is None or list_of_ints[0] < element, set list_of_ints[0] = element
            if highest_val_list[0] is None or highest_val_list[0] < element:
                highest_val_list[0] = element
                continue

        # [5, 9, 16]
        lowest_of_two_product = self.getLowestOfTwoProduct(list_of_ints)
        total_product = functools.reduce(lambda x,y: x * y, highest_val_list)

        if lowest_of_two_product * highest_val_list[2] > total_product:
            total_product = lowest_of_two_product * highest_val_list[2]

        return total_product

    def getLowestOfTwoProduct(self, list_of_ints):
        lowest_of_two_list = [None, None]

        for element in list_of_ints:
            if lowest_of_two_list[1] is None or lowest_of_two_list[1] > element:
                lowest_of_two_list[0] = lowest_of_two_list[1]
                lowest_of_two_list[1] = element
                continue

            if lowest_of_two_list[0] is None or lowest_of_two_list[0] > element:
                lowest_of_two_list[0] = element

        return functools.reduce(lambda x,y: x * y, lowest_of_two_list)


if __name__ == '__main__':

    case_1 = [9, 1, 5, 16, 2, 3]
    case_2 = [-10,-10, 3, 1, 5, 2]

    expected_1 = 720
    expected_2 = 500

    solution_1 = Solution().highestProductOf3(case_1)
    solution_2 = Solution().highestProductOf3(case_2)

    print(solution_1)
    print(solution_2)

    assert expected_1 == solution_1
    assert expected_2 == solution_2

