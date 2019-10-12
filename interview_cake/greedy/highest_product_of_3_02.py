# Highest Product of 3
#
#
# Given a list of integers, find the highest product you can get from three of
# the integers.
#
# The input list_of_ints will always have at least three integers.
#
# Example
#
# [9, 1, 5, 16, 2, 3] --> 16 * 9 * 5 = 720
#
#
# Brute force solution
#   1. Use three pointers. Use first to find the highest number
#   2. Use second pointer to find the second highest number
#   3. Use third pointer to find the third highest number
#
# This is the  time complexity of O(N^3) and spatial complexity of O(1).
#
# Can we do better? YES!!!
#   - using greedy algorithm, we can use one time pass to reduce time complexity to O(N)!
#
# Improved pseudcode
#   1. create an array highest_val_list = [third_highest, second_highest, highest] of highest values
#     highest_val_list = [None, None, None]
# #   2. for each element in array
#     for element in highest_val_list:
#         #   2.1 if highest_val_list is empty, then add the element to highest
#         #   2.2 if highest_val_list is not empty, then compare val with the highest. if val > highest, then replace val with highest, and propagate the rest
#         if highest_val_list[2] == None or element > highest_val_list[2]:
#             highest_val_list[0] = highest_val_list[1]
#             highest_val_list[1] = highest_val_list[2]
#             highest_val_list[2] = element
#             continue

#         #   2.3 repeat the same with other values if val < highest
#         if highest_val_list[1] == None or element > highest_val_list[1]:
#             highest_val_list[0] = highest_val_list[1]
#             highest_val_list[1] = element
#             continue

#         #   2.3 repeat the same with other values if val < highest
#         if highest_val_list[1] == None or element > highest_val_list[1]:
#             highest_val_list[0] = element
#             continue

#     total_product = functools.reduce(lambda x,y: x*y, highest_val_list)

#     return total_product

import functools

class Solution:
    def highestProductOf3(self, list_of_ints):
    #   1. create an array highest_val_list = [third_highest, second_highest, highest] of highest values
        highest_val_list = [None, None, None]

    #   2. for each element in array
        for element in list_of_ints:
            #   2.1 if highest_val_list is empty, then add the element to highest
            #   2.2 if highest_val_list is not empty, then compare val with the highest. if val > highest, then replace val with highest, and propagate the rest
            if highest_val_list[2] == None or element > highest_val_list[2]:
                highest_val_list[0] = highest_val_list[1]
                highest_val_list[1] = highest_val_list[2]
                highest_val_list[2] = element
                continue

            #   2.3 repeat the same with other values if val < highest
            if highest_val_list[1] == None or element > highest_val_list[1]:
                highest_val_list[0] = highest_val_list[1]
                highest_val_list[1] = element
                continue

            #   2.3 repeat the same with other values if val < highest
            if highest_val_list[1] == None or element > highest_val_list[1]:
                highest_val_list[0] = element
                continue

        lowest_product_of_two = self.getLowestProductOfTwo(list_of_ints)
        total_product = functools.reduce(lambda x,y: x*y, highest_val_list)

        if lowest_product_of_two > 0 and lowest_product_of_two * highest_val_list[-1] > total_product:
            total_product = lowest_product_of_two * highest_val_list[-1]

        return total_product

    def getLowestProductOfTwo(self, list_of_ints):
        lowest_val_list = [None, None]

        for element in list_of_ints:
            if lowest_val_list[1] == None or element < lowest_val_list[1]:
                lowest_val_list[0] = lowest_val_list[1]
                lowest_val_list[1] = element
                continue

            if lowest_val_list[0] == None or element < lowest_val_list[0]:
                lowest_val_list[0] = element

        return functools.reduce(lambda x,y: x*y, lowest_val_list)


if __name__ == '__main__':

    case_1 = [9, 1, 5, 16, 2, 3]
    case_2 = [-10,-10, 3, 1, 5, 2]

    expected_1 = 720
    expected_2 = 500

    solution_1 = Solution().highestProductOf3(case_1)
    solution_2 = Solution().highestProductOf3(case_2)

    assert expected_1 == solution_1
    assert expected_2 == solution_2

