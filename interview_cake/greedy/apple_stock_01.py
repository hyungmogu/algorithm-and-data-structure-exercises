# Apple Stock
#
#
# Write an efficient function that takes stock_prices and returns the best profit
# I could have made from [one] purchase and [one] sale of one share of Apple stock yesterday.
#
# Example
#   stock_prices = [10, 7, 5, 8, 11, 9]
#   Solution().get_max_profit(stock_prices) -> 6
#
#   [10, 7, 8, 11, 9]
#                  x
#                  ^
# Brute force solution
#   1. for each i in arr
#   2. for each j in arr
#   3. if j =< i, continue
#   4. if arr[j] - arr[i] > max_price, then replace max_price with arr[j] - arr[i]
#   5. return max_price
#
#   Time complexity is O(N^2), spatial complexity O(1)
#
#   Can we do better? YES!!! --> Greedy algorithm
#
# Improved solution
#   1. for each element x in arr
#   2. evaluate the current profit (current_profit = current_price - min_price)
#   3. determine max_profit (max_profit = max(current_profit, max_profit))
#   4. determine min_profit (min_price = min(current_price, min_price))
#
#   Time Complexity O(N) and spatial complexity of O(1)
#
# Example 2
#   stock_prices = [7, 1, 5, 3, 4, 6]
#   Solution().get_max_profit(stock_prices) -> 5
#
# Example 3
#   stock_prices = [5, 4, 3, 2, 1]
#   Solution().get_max_profit(stock_prices) -> 0
#
# Example 4
#   stock_prices = [1, 2, 3, 4, 5]
#   Solution().get_max_profit(stock_prices) -> 4
#
# Example 5
#   stock_prices = [1, 1, 1, 1, 1]
#   Solution().get_max_profit(stock_prices) -> 0


class Solution:
    # [10, 7, 8, 11, 9]
    def appleStock(self, stock_prices):
        if len(stock_prices) < 2:
            return 0

        max_profit = 0
        min_price = stock_prices[0]

        #   1. for each element x in arr
        for current_price in stock_prices:
        #   2. evaluate the current profit (current_profit = current_price - min_price)
            current_profit = current_price - min_price

        #   3. determine max_profit (max_profit = max(current_profit, max_profit))
            max_profit = max(current_profit, max_profit)

        #   4. determine min_price (min_price = min(current_price, min_price))
            min_price = min(current_price, min_price)

        return max_profit

if __name__ == '__main__':
    case_1 = [10, 7, 5, 8, 11, 9]
    case_2 = [7, 1, 5, 3, 4, 6]
    case_3 = [5, 4, 3, 2, 1]
    case_4 = [1, 2, 3, 4, 5]
    case_5 = [1, 1, 1, 1, 1]

    expected_1 = 6
    expected_2 = 5
    expected_3 = 0
    expected_4 = 4
    expected_5 = 0

    solution_1 = Solution().appleStock(case_1)
    solution_2 = Solution().appleStock(case_2)
    solution_3 = Solution().appleStock(case_3)
    solution_4 = Solution().appleStock(case_4)
    solution_5 = Solution().appleStock(case_5)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4
    assert expected_5 == solution_5

