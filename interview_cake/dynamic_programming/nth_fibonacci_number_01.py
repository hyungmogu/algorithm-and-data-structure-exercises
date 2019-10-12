# nth fibonacci number
#
# Write a function fib() that takes an integer n and returns the nth Fibonacci
# number.
#
#  n = 0              1
#  n = 1            1     1
#  n = 2         1     2     1
#  n = 3      1     3     3      1
#
# fib(n) = fib(n - 1) + f(n - 2)
#
# Brute force solution
# 1. if at base case (n = 0, or n = 1) return 1

    # if n == 0 or n == 1:
    #     return 1

# 2. otherwise, return fib(n - 1) + fib(n - 2)
    # return self.fib(n - 1)(fib (n - 2) + fib(n - 3)) + self.fib(n - 2)

# time complexity O(2^N) spatial complexity O(2^N)
#
# Can we make it better? --> YES!
#   - Memoization!!
#       - stores the result of nth value of recursion in dictionary --> avoids repeat recursion
#       - this helps to run recursion only once per unique value
#
# time complexity O(N) and O(N)
#
#
# __init__
    # self.memoization = {}

#  1. if at base case (n = 0, or n = 1) return 1

    # if n == 0 or n == 1:
    #     return 1

#  2. check memoization and see if value for nth fibonacci number exists
    # if n in self.memoization:
    #     return self.memoization[n]

    # nth_fib = self.fib(n - 1) + self.fib(n - 2)

    # self.memoization[n] = nth_fib

    # return nth_fib


#  2.1 if yes, return the value
#  2.2 else, return fib(n-1) + fib(n-2)



class Solution:
    def __init__(self):
        self.memoization = {}

    def fib(self, n):
        #  1. if at base case (n = 0, or n = 1) return 1

        if n == 0 or n == 1:
            return 1

        #  2. check memoization and see if value for nth fibonacci number exists
        if n in self.memoization:
            return self.memoization[n]

        nth_fib = self.fib(n - 1) + self.fib(n - 2)

        self.memoization[n] = nth_fib

        return nth_fib


if __name__ == '__main__':
    case_1 = 0
    case_2 = 0
    case_3 = 100
    case_4 = 3

    expected_1 = 1
    expected_2 = 1
    expected_3 = 573147844013817084101
    expected_4 = 3

    solution_1 = Solution().fib(case_1)
    solution_2 = Solution().fib(case_2)
    solution_3 = Solution().fib(case_3)
    solution_4 = Solution().fib(case_4)

    assert solution_1 == expected_1
    assert solution_2 == expected_2
    assert solution_3 == expected_3
    assert solution_4 == expected_4
