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
#   Take Out Orders: [1, 3, 5]
#                              x
#   Dine In Orders: [2, 4, 6]
#                              x
#   Served Orders: [1, 2, 4, 6, 5, 3]
#                                     ^
# Brute Force Solution

def cafeOrderChecker(self, take_out_orders, dine_in_orders, served_orders):
    index_takeout = 0
    index_dine_in = 0
    index_served_orders = 0

    #   1. for each item in Served Orders
    while index_served_orders < len(served_orders):
        #   1.1. If take_out_orders[index_takeout] == served_orders[index_served_orders],
        #   then increment index_takeout, and index_served_orders and continue
        if index_takeout < len(take_out_orders) and take_out_orders[index_takeout] == served_orders[index_served_orders]:
            index_takeout +=1
            index_served_orders += 1
            continue

        #   1.2. If dine_in_orders[index_dine_in] == served_orders[index_served_orders],
        #   then increment index_dine_in, and index_served_orders and continue
        print(index_served_orders)
        print(index_dine_in)
        if index_dine_in < len(dine_in_orders) and dine_in_orders[index_dine_in] == served_orders[index_served_orders]:
            index_dine_in += 1
            index_served_orders += 1
            continue

        #   1.3. return false otherwise
        return False

    if index_dine_in < len(dine_in_orders) or index_takeout < len(take_out_orders):
        return False

    #   2. return true
    return True

# has O(M) time complexity

class Solution:
    def cafeOrderChecker(self, take_out_orders, dine_in_orders, served_orders):
        index_takeout = 0
        index_dine_in = 0
        index_served_orders = 0

        #   1. for each item in Served Orders
        while index_served_orders < len(served_orders):
            #   1.1. If take_out_orders[index_takeout] == served_orders[index_served_orders],
            #   then increment index_takeout, and index_served_orders and continue
            if index_takeout < len(take_out_orders) and take_out_orders[index_takeout] == served_orders[index_served_orders]:
                index_takeout +=1
                index_served_orders += 1
                continue

            #   1.2. If dine_in_orders[index_dine_in] == served_orders[index_served_orders],
            #   then increment index_dine_in, and index_served_orders and continue
            if index_dine_in < len(dine_in_orders) and dine_in_orders[index_dine_in] == served_orders[index_served_orders]:
                index_dine_in += 1
                index_served_orders += 1
                continue

            #   1.3. return false otherwise
            return False

        # 2. If extra orders were made after hours, then return false
        if index_dine_in < len(dine_in_orders) or index_takeout < len(take_out_orders):
            return False

        #   3. return true
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