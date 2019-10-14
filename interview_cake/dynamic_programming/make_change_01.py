# Make Change
#
# Your quirky boss collects rare, old coins...
#
# They found out you're a programmer and asked you to solve something they've
# been wondering for a long time.
#
# Write a function that, given:
#
# an amount of money
# a list of coin denominations
# computes the number of ways to make the amount of money with coins of the
# available denominations.
#
# Example: for amount=44 (44¢) and denominations=[1,2,3][1,2,3] (11¢, 22¢ and 33¢),
# your program would output 44—the number of ways to make 44¢ with those denominations:
#
# 1¢, 1¢, 1¢, 1¢
# 1¢, 1¢, 2¢
# 1¢, 3¢
# 2¢, 2¢
#
#

class Solution:
    def __init__(self):
        self.memo = {}
    def makeChange(self, coins, coin_index, amount):
        if amount == 0:
            return 1

        if amount < 0:
            return 0

        if coin_index <= 0:
            return 0

        if '{} {}'.format(coin_index, amount) in self.memo:
            return self.memo['{} {}'.format(coin_index, amount)]

        numChanges = self.makeChange(coins, coin_index - 1, amount) + self.makeChange(coins, coin_index, amount - coins[coin_index - 1])

        self.memo['{} {}'.format(coin_index, amount)] = numChanges

        return numChanges


if __name__ == "__main__":
    amount_1 = 4
    coins_1 = [1,2,3]
    coin_index_1 = len(coins_1)

    expected_1 = 4

    solution_1 = Solution().makeChange(coins_1, coin_index_1, amount_1)

    assert solution_1 == expected_1
