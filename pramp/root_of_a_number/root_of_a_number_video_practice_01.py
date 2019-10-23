# Root of a Number
#
# Given a non-negative float x, find it's nth root
#
# input
#   - x (float)
#   - n (integer)
#
# output
#   - float
#
# constraints
#   - |y-root(x,n)| < 0.001
#   - power (**) is allowed
#
#
# input:  x = 7, n = 3
# output: 1.913
#
# input:  x = 9, n = 2
# output: 3
#
# input: x = 1/4, n = 2
# output: 0.5
#
# input: x = 1, n = 100
# output: 1
#
# input: x = 0, n = 1000
# output: 0
#
#
# cases
#   1. any x, n = 0
#   2. x == 0, n is any
#   3. x == 1, n is any
#   4. 0 < x < 1, n is any
#   5. x > 1 , n is any
# n = 2 x = 9
# n - 2 x = 0.1
#          0.5 --> 0.25
# | ---------------------------------- |
# 0    0.1                            9
#                   1    3
#          ceiling = middle
#
# Psuedocode (binary search algorithm -> O(lg n) Time Complexity, O(1) spatial complexity)

class Solution:
    def solve(self, x, n):
        #   1. if n == 0, return 1
        if n == 0:
            return 1

        #   2. if x == 0, return 0
        if x == 0:
            return 0

        #   3. if x == 1, return 1
        if x == 1:
            return 1

        if x > 1:
            floor = 1
            ceiling = x
        else:
            floor = 0
            ceiling = 1

        solution = x

        #   4. initialize floor and celing (floor = 1, ceiling = x if x > 1) and (floor = 0, ceiling = 1, if 0 < x < 1)
        #   5. While True:
        while True:
            #   6. find middle
            half_distance = (ceiling - floor) / 2.0
            middle = floor + half_distance

            #   7. find guess
            guess = middle ** (n)

            #   8. if guess is solution, then return middle
            if abs(guess - solution) < 0.001:
                return round(middle,3)

            #   9. if guess is not solution and guess > solution,
            if guess > solution:
                ceiling = middle

            #   10. if guess is not solution and guess < solution,
            if guess < solution:
                floor = middle


if __name__ == '__main__':
    case_1 = 4
    case_2 = 7
    case_3 = 9
    case_4 = 0.2
    case_5 = 0
    case_6 = 1

    expected_1 = 2.0
    expected_2 = 1.913
    expected_3 = 2.080
    expected_4 = 0.447
    expected_5 = 0
    expected_6 = 1

    result_1 = Solution().solve(case_1, 2)
    print(result_1)
    result_2 = Solution().solve(case_2, 3)
    result_3 = Solution().solve(case_3, 3)
    result_4 = Solution().solve(case_4, 2)
    result_5 = Solution().solve(case_5, 2)
    result_6 = Solution().solve(case_6, 10)

    assert expected_1 == result_1
    assert expected_2 == result_2
    assert expected_3 == result_3
    assert expected_4 == result_4
    assert expected_5 == result_5
    assert expected_6 == result_6
