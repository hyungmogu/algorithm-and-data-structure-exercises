# Cafe Order Checker
#
# My cake shop is so popular, I'm adding some tables and hiring wait staff so
# folks can have a cute sit-down cake-eating experience.
#
# I have two registers: one for take-out orders, and the other for the other
# folks eating inside the cafe. All the customer orders get combined into one
# list for the kitchen, where they should be handled first-come, first-served.
#
# Recently, some customers have been complaining that people who placed orders
# after them are getting their food first. Yikes—that's not good for business!

# To investigate their claims, one afternoon I sat behind the registers with my
# laptop and recorded:

# The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
# The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
# Each customer order (from either register) as it was finished by the kitchen. (served_orders)
# Given all three lists, write a function to check that my service is first-come,
# first-served. All food should come out in the same order customers requested it.

# We'll represent each customer order as a unique integer.

# As an example,
#

#   Take Out Orders: [1, 3, 5]
#   Dine In Orders: [2, 4, 6]
#   Served Orders: [1, 2, 4, 6, 5, 3]
# would not be first-come, first-served, since order 3 was requested before
# order 5 but order 5 was served first.

# But,

#   Take Out Orders: [1, 3, 5]
#   Dine In Orders: [2, 4, 6]
#   Served Orders: [1, 2, 3, 5, 4, 6]
#
# would be first-come, first-served.
#
# Input
#   - list of integers x 3
# Output
#    - Boolean
#
# Constraints
#   - there can be extra orders at the end of the day (len(take_out_orders) or len(dine_in_orders) > len(served_orders))
#
#
#
#   Take Out Orders: [1, 3, 5]
#                        x
#   Dine In Orders: [2, 4, 6]
#                             x
#   Served Orders: [1, 2, 4, 6, 5, 3]
#                                     ^
# Brute Force Solution
# def cafeOrderChecker(self, take_out_orders, dine_in_orders, served_orders):
#     #`  1. while index_served_orders < len(served_orders)
#     index_served_orders = 0
#     index_dine_in = 0
#     index_take_out = 0

#     while index_served_orders < len(served_orders):

#         #   2. if index_take_out < len(take_out_orders) and served_orders[index_served_orders] == take_out_orders[index_take_out]
#         if index_take_out < len(take_out_orders) and served_orders[index_served_orders] == take_out_orders[index_take_out]:
#             #   2.1 increment index_served_orders
#             #   2.2 increment index_take_out
#             index_served_orders += 1
#             index_take_out += 1
#             continue

#         #   2.3 if index_dine_in < len(dine_in_orders) and served_orders[index_served_orders] == dine_in_orders[index_dine_in]
#         if index_dine_in < len(dine_in_orders) and served_orders[index_served_orders] == dine_in_orders[index_dine_in]:
#             #   2.4 increment index_dine_in
#             #   2.5 increment index_served_orders
#             index_dine_in += 1
#             index_served_orders +=1
#             continue
#         #

#         #   2.5 return False
#         return False

#     #   3. if index_dine_in < len(dine_in) or index_take_out < len(take_Out)
#     if index_dine_in < len(dine_in) or index_take_out < len(take_Out):
#         return False

#     #   3.1 return False
#     return True
# #   4. return True
#
# Time complexity of O(N) and spatial complexity of O(1)

class Solution:
    def cafeOrderChecker(self, take_out_orders, dine_in_orders, served_orders):
        #`  1. while index_served_orders < len(served_orders)
        index_served_orders = 0
        index_dine_in = 0
        index_take_out = 0

        while index_served_orders < len(served_orders):

            #   2. if index_take_out < len(take_out_orders) and served_orders[index_served_orders] == take_out_orders[index_take_out]
            if index_take_out < len(take_out_orders) and served_orders[index_served_orders] == take_out_orders[index_take_out]:
                #   2.1 increment index_served_orders
                #   2.2 increment index_take_out
                index_served_orders += 1
                index_take_out += 1
                continue

            #   2.3 if index_dine_in < len(dine_in_orders) and served_orders[index_served_orders] == dine_in_orders[index_dine_in]
            if index_dine_in < len(dine_in_orders) and served_orders[index_served_orders] == dine_in_orders[index_dine_in]:
                #   2.4 increment index_dine_in
                #   2.5 increment index_served_orders
                index_dine_in += 1
                index_served_orders +=1
                continue
            #

            #   2.5 return False
            return False

        #   3. if index_dine_in < len(dine_in) or index_take_out < len(take_Out)
        if index_dine_in < len(dine_in) or index_take_out < len(take_Out):
            return False

        #   3.1 return False
        return True


if __name__ =='__main__':
    take_out_orders_1 = [1, 3, 5]
    take_out_orders_2 = [1, 3, 5]
    take_out_orders_3 = [1, 3, 5, 7]

    dine_in_orders_1 = [2, 4, 6]
    dine_in_orders_2 = [2, 4, 6]
    dine_in_orders_3 = [2, 4, 6, 8]

    served_orders_1 = [1, 2, 4, 6, 5, 3]
    served_orders_2 = [1, 2, 3, 5, 4, 6]
    served_orders_3 = [1, 2, 3, 5, 4, 6]

    expected_1 = False
    expected_2 = True
    expected_3 = False

    solution_1 = Solution().cafeOrderChecker(take_out_orders_1, dine_in_orders_1, served_orders_1)
    solution_2 = Solution().cafeOrderChecker(take_out_orders_2, dine_in_orders_2, served_orders_2)
    solution_3 = Solution().cafeOrderChecker(take_out_orders_3, dine_in_orders_3, served_orders_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3




