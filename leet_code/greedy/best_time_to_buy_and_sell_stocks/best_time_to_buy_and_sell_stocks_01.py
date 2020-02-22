# Best Time to Buy and Sell Stock II
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
#
#
# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
#
# Example 2:
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
#
# Example 3:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# How greedy algorithm works
#   1.
#   2.

class Solution:
    def maxProfit(self, prices):
        # 1. find value via simple one pass
        profit_simple_one_pass = self.get_profit_simple_one_pass(prices)
        # 2. find value via peak valley approach
        profit_peak_valley = self.get_profit_peak_valley(prices)
        # 3. compare the two, return the largest

        return profit_simple_one_pass if profit_simple_one_pass > profit_peak_valley else profit_peak_valley

    def get_profit_simple_one_pass(self, prices):
        # find the index of minimum value



        # find the index of maximum value

        # if index_minimum < index_maximum, then return maximum - minimum

        # else return 0
