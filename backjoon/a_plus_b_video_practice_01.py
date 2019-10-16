# A + B
#
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
#
# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 출력
# 첫째 줄에 A+B를 출력한다.
#
#
# 예제 입력 1
# 1 2
#
# 예제 출력 1
# 3
#
# Pseudocode
#   1. 입력한것을 array로 바꾼다
#   2. Array에 있는 string을 integer로 바꾼다
#     integers = [int(x) for x in input().split()]

# #   3. Array안에 있는 integer를 합친다
#     total = sum(integers)

# #   4. 합을 return
#     return total

from unittest.mock import patch

class Solution:
    def aPlusB(self):
        #   1. 입력한것을 array로 바꾼다
        #   2. Array에 있는 string을 integer로 바꾼다
        integers = [int(x) for x in input().split()]

        #   3. Array안에 있는 integer를 합친다
        total = sum(integers)

        #   4. 합을 return
        return total



if __name__ == "__main__":
    case_1 = [
        '1 2'
    ]

    expected = 3

    with patch('builtins.input', side_effect=case_1):
        answer = Solution().aPlusB()

        assert answer == expected
