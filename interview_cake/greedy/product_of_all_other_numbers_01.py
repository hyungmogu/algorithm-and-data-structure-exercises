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
# Here's the catch: You can't use division in your solution!
#
#
# Example
    # #   1. while index_i == 0 and index_i < len(arr), multiply element at index_i with all other elements
    # #   1.1. store result in array product_of_others_1 = [1, first_element, first_element * second_element, ... , first_element * second_element * ... * second_last_element]
    # product_of_others_1 = [1] * len(arr)
    # current_product_1 = 1
    # index_i = 1

    # while index_i < len(arr):
    #     current_product_1 *= arr[index_i - 1]
    #     product_of_others_1[index_i] = current_product_1

    #     index_i += 1

    # #   2. while index_j == len(arr) - 1 and index_j > 0, multiply element at index_j with all other elements
    # #   2.1 store result in array products_of_others_2 = [last_element * ... * second_element, last_element * second_last_element,last_element,1]
    # product_of_others_2 = [1] * len(arr)
    # current_product_2 = 1
    # index_j = len(arr) - 2

    # while index_j > -1:
    #     current_product_2 *= arr[index_j + 1]
    #     product_of_others_2[index_j] = current_product_2

    #     index_j -= 1

    # #   3. multiply each element in product_of_others_1 and products_of_others_2
    # product_of_others = [1] * len(arr)

    # for index, value in enumerate(product_of_others):
    #     product_of_others[index] = product_of_others_1[index] * product_of_others_2[index]

    # #   4. return result
    # return product_of_others

class Solution:
    def productOfAllOtherNumbers(self, arr):
        product_of_others_1 = [1] * len(arr)
        current_product_1 = 1
        index_i = 1

        while index_i < len(arr):
            current_product_1 *= arr[index_i - 1]
            product_of_others_1[index_i] = current_product_1

            index_i += 1

        #   2. while index_j == len(arr) - 1 and index_j > 0, multiply element at index_j with all other elements
        #   2.1 store result in array products_of_others_2 = [last_element * ... * second_element, last_element * second_last_element,last_element,1]
        product_of_others_2 = [1] * len(arr)
        current_product_2 = 1
        index_j = len(arr) - 2

        while index_j > -1:
            current_product_2 *= arr[index_j + 1]
            product_of_others_2[index_j] = current_product_2

            index_j -= 1

        #   3. multiply each element in product_of_others_1 and products_of_others_2
        product_of_others = [1] * len(arr)

        for index, value in enumerate(product_of_others):
            product_of_others[index] = product_of_others_1[index] * product_of_others_2[index]

        #   4. return result
        return product_of_others

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