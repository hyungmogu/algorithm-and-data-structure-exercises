# Root of Number

# given a positive float x, we are to find its nth root.
#

# input:  x = 7, n = 3
# output: 1.913

# input:  x = 9, n = 2
# output: 3

# [time limit] 5000ms
#
# 입력
# float x
#
# 0 <= x
# integer n
#
# 출력
# 0 < n
#  float

# 제약
#   1. x 의 값은 0 이상 이다

# 경우
#   1. if n == 0 and x is any
#   2. if n != 0, and x == 0
#   3. if n != 0, and x == 1
#   4. if n != 0, and 0 < x < 1
#   5. if n != 0, and x > 1

# 수도코드
class Solution:
    def solve(self, x, n):
        #   1. if n == 0, 1 을 리턴한다
        if n == 0:
            return 1

        #   2. if n != 0, and x == 0, 0를 리턴한다
        if n != 0 and x == 0:
            return 0

        #   3. if n != 0, and x == 1, 1을 리턴한다
        if n != 0 and x == 1:
            return 1

        return self.nthRoot(x, n)

    def nthRoot(self, x, n):
        solution = x
        # 1. initialize floor = 0 and ceiling = x
        if x > 1:
            floor = 1
            ceiling = x
        else:
            floor = 0
            ceiling = 1

        # 2. floor와 ceiling 사이에 있는 값을 구한다. 그리고 그 값을 middle에 저장한다

        while True:

            half_distance = (ceiling - floor) / 2.0
            middle = floor + half_distance

            # 3. middle 을 이용해 guess 값을 구한다
            guess = middle ** (n)

            # 4. if guess 가 정답이면, guess 를 리턴한다
            print(middle)
            if abs(guess - solution) < 0.001:
                return round(middle, 3)

            # 5. if guess 가 정답이 아니고
            #   5.1 and if guess < solution,
            if guess != x and guess < solution:
                floor = middle

            #   5.2 and if guess > solution, ceiling = middle 로 한다
            if guess != x and guess > solution:
                ceiling = middle



# =========================================================

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