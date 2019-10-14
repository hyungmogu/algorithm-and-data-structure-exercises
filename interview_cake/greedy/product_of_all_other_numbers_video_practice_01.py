# Product of all other numbers
#
# Write a function get_products_of_all_ints_except_at_index() that takes a list
# of integers and returns a list of the products.
#
# For example, given:
#
#   [1, 7, 3, 4]
#
# your function would return:
#
#   [84, 12, 28, 21]
#
# by calculating:
#
#   [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
#
#   None         1              1 * 7       1 * 7 * 3
#
#  4 * 3 * 7   4 * 3              4             None
#
# Brute Force
#   1. for each element at index_i,
#   1.1 walk through all elements except at index_i, and get its product
#   1.2 append the product to list product_of_all_others
#   2. product_of_all_others
#
# time complexity is O(N^2) and spatial complexity of O(N)
#
# The time complexity can be reduced to O(N)
#
#
# Improved solution
#     index_i = 1
#     index_j = len(arr) - 2

#     current_product_1 = 1
#     current_product_2 = 1

#     product_of_all_others_1 = [1] * len(arr)
#     product_of_all_others_2 = [1] * len(arr)
#     product_of_all_others = [1] * len(arr)

# #   1. while index_i == 1 and index_i < len(arr)
#     while index_i < len(arr):
#         #   1.1 get current_product_1 (current_product_1 *= arr[index_i-1])
#         current_product_1 *= arr[index_i-1]
#         #   1.2 set current_product_1 to product_of_all_others_1[index_i]
#         product_of_all_others_1[index_i] = current_product_1

#         index_i += 1

#     #   2. while index_j == len(arr) - 2 and index_j > -1
#     while index_j > -1:
#         #   2.1 get current_product_2 (current_product_2 *= arr[index_j+1])
#         current_product_2 *= arr[index_j+1]
#         #   2.2 set current_product_2 to product_of_all_others_2[index_j]
#         product_of_all_others_2[index_j] = current_product_2

#         index_j -= 1

# #   3. for each element and index in both 'product_of_all_others_1' and 'product_of_all_others_2'

#     for index in range(product_of_all_others):
#         product_of_all_others[index] = product_of_all_others_1[index] * product_of_all_others_2[index]

# #   4. return product_of_all_others
#     return product_of_all_others
# Here's the catch: You can't use division in your solution!

class Solution:
    def productOfAllOtherNumbers(self, arr):
        index_i = 1
        index_j = len(arr) - 2

        current_product_1 = 1
        current_product_2 = 1

        product_of_all_others_1 = [1] * len(arr)
        product_of_all_others_2 = [1] * len(arr)
        product_of_all_others = [1] * len(arr)

        #   1. while index_i == 1 and index_i < len(arr)
        while index_i < len(arr):
            #   1.1 get current_product_1 (current_product_1 *= arr[index_i-1])
            current_product_1 *= arr[index_i-1]
            #   1.2 set current_product_1 to product_of_all_others_1[index_i]
            product_of_all_others_1[index_i] = current_product_1

            index_i += 1

        #   2. while index_j == len(arr) - 2 and index_j > -1
        while index_j > -1:
            #   2.1 get current_product_2 (current_product_2 *= arr[index_j+1])
            current_product_2 *= arr[index_j+1]
            #   2.2 set current_product_2 to product_of_all_others_2[index_j]
            product_of_all_others_2[index_j] = current_product_2

            index_j -= 1

        #   3. for each element and index in both 'product_of_all_others_1' and 'product_of_all_others_2'
        for index in range(len(product_of_all_others)):
            product_of_all_others[index] = product_of_all_others_1[index] * product_of_all_others_2[index]

        #   4. return product_of_all_others
        return product_of_all_others


if __name__ == '__main__':
    case_1 = [1, 7, 3, 4]
    case_2 = [1]
    case_3 = []

    expected_1 = [84, 12, 28, 21]
    expected_2 = [1]
    expected_3 = []

    solution_1 = Solution().productOfAllOtherNumbers(case_1)
    solution_2 = Solution().productOfAllOtherNumbers(case_2)
    solution_3 = Solution().productOfAllOtherNumbers(case_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3