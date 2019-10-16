# A-B
#
# 문제
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10) (정수)
#
# 출력
# 첫째 줄에 A-B를 출력한다. (정수)
#
# 예제 입력 1
# 3 2
# 예제 출력 1
# 1
#
# pseudocode
# def aMinusB(self):
# #   1. input을 통해 integer A 와 B 를 문자열로 입력받는다
# #   2. 문자열을 integer 배열로 환산한다 (변수 이름을 'numbers'로 한다)
#     numbers = [int(x) for x in input().split()]

# #   3. A 와 B의 차액을 구한다 (numbers[0] - numbers[1]) 그리고 값을 return 한다
#     return numbers[0] - numbers[1]

from unittest.mock import patch

class Solution:
    def aMinusB(self):
        #   1. input을 통해 integer A 와 B 를 문자열로 입력받는다
        #   2. 문자열을 integer 배열로 환산한다 (변수 이름을 'numbers'로 한다)
        numbers = [int(x) for x in input().split()]

        #   3. A 와 B의 차액을 구한다 (numbers[0] - numbers[1]) 그리고 값을 return 한다
        return numbers[0] - numbers[1]

if __name__ == "__main__":
    case_1 = [
        '1 2'
    ]

    case_2 = [
        '4 3'
    ]

    expected_1 = -1
    expected_2 = 1

    with patch('builtins.input', side_effect=case_1):
        answer_1 = Solution().aMinusB()

        assert answer_1 == expected_1

    with patch('builtins.input', side_effect=case_2):
        answer_2 = Solution().aMinusB()

        assert answer_2 == expected_2
