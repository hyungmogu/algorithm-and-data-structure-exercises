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
# Example: for amount=4 (4¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢),
# your program would output 4—the number of ways to make 4¢ with those denominations:
#
# 1. 1¢, 1¢, 1¢, 1¢
# 2. 1¢, 1¢, 2¢
# 3. 1¢, 3¢
# 4. 2¢, 2¢
#
# coins = [1,2,3]
# amount = 4
#
#
# input
#   - coins / denominations (list of integers)
#   - amount (integer)
#
# output
#   - integer (number of possibilities denominations could have that will add to amount)
#
# constraints
#   - combination of demominations must be unique
#   - there are infinitely many coins available
#
#
#
#
# Example
#   n = 4
#   coins = [1,2]
#
#  1 + 1 + 1 + 1          1 + 1 + 1 + 1
#  1 + 1 + 2         -->  2 + 1 + 1
#  1 + 2 + 1              2 + 2
#  2 + 1 + 1
#  2 + 2
#
#  ...
#  2 + 2 + 1
#
# Improved solution (covering uniqueness)
#   1.
#
#
# __init__


class Solution:
    def __init__(self):
        self.memo = {}

    def makeChange(self, coins, current_coin_index, current_amount):
        # Brute force solution
        # 1. if amount == 0, return 1
        if current_amount == 0:
            return 1
        # 2. if amount < 0, return 0
        if current_amount < 0:
            return 0

        if current_coin_index < 0:
            return 0

        if '{}'.format(current_amount) in self.memo:
            return self.memo['{} {}'.format(current_amount, current_coin_index)]

        # 3. Use modified fibonacci sum to get 'numChanges' (self.makeChange(coins, current_amount - 1) + self.makeChange(coins, current_amount -2) + self.makeChange(coins, current_amount -3))
        numChanges = 0
        for coin_index in reversed(range(0, current_coin_index + 1)):
            numChanges += self.makeChange(coins, coin_index, current_amount - coins[coin_index])

        self.memo['{} {}'.format(current_amount, current_coin_index)] = numChanges

        return numChanges

        # 4. return numChanges


if __name__ == "__main__":
    amount_1 = 4
    coins_1 = [1,2,3]
    coin_index_1 = len(coins_1) - 1
    expected_1 = 4

    solution_1 = Solution().makeChange(coins_1, coin_index_1, amount_1)
    print(solution_1)
    assert solution_1 == expected_1




