# 아스키 코드
#
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.
#
# 입력
# 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.
#
# 출력
# 입력으로 주어진 글자의 아스키 코드 값을 출력한다.
#
# constraint
#   - 알파벳, 소문자 대문자 중에 하나가 입력된다
#
#
# 예제 입력 1
# A
# 예제 출력 1
# 65
# 예제 입력 2
# C
# 예제 출력 2
# 67
# 예제 입력 3
# 0
# 예제 출력 3
# 48
# 예제 입력 4
# 9
# 예제 출력 4
# 57
# 예제 입력 5
# a
# 예제 출력 5
# 97
# 예제 입력 6
# z
# 예제 출력 6
# 122
#
#
# pseudocode
# def getInput(self):
#     container = []
#     while True:
#         try:
#             line = input()
#         except Exception:
#             break

#         container.append(line)

#     return container

# def asciiCode(self, character):
#     #   1. input() 을 이용해 입력정보를 받는다. 그리고 이 정보를 변수 'symbol'에 저장한다
#     symbol = self.getInput()[0]

#     #   2. symbol에 있는 정보를 ascii 로 바꾼다 (ord(symbol --> ascii), chr(ascii --> symbol))
#     symbol_ascii = ord(symbol)

#     #   3. 아스키를 return 한다
#     return symbol_ascii
#
# 시간복잡도 -> O(1), 공간복잡도 -> O(1)

from unittest.mock import patch

class Solution:
    def asciiCode(self):
        #   1. input() 을 이용해 입력정보를 받는다. 그리고 이 정보를 변수 'symbol'에 저장한다
        symbol = self.getInput()[0]

        #   2. symbol에 있는 정보를 ascii 로 바꾼다 (ord(symbol --> ascii), chr(ascii --> symbol))
        symbol_ascii = ord(symbol)

        #   3. 아스키를 return 한다
        return symbol_ascii


    def getInput(self):
        container = []
        while True:
            try:
                line = input()
            except Exception:
                break

            container.append(line)

        return container


if __name__ == '__main__':
    case_1 = ['A']
    case_2 = ['C']
    case_3 = ['0']
    case_4 = ['9']
    case_5 = ['a']
    case_6 = ['z']

    expected_1 = 65
    expected_2 = 67
    expected_3 = 48
    expected_4 = 57
    expected_5 = 97
    expected_6 = 122

    with patch('builtins.input', side_effect=case_1):
        answer_1 = Solution().asciiCode()
        assert answer_1 == expected_1

    with patch('builtins.input', side_effect=case_2):
        answer_2 = Solution().asciiCode()
        assert answer_2 == expected_2

    with patch('builtins.input', side_effect=case_3):
        answer_3 = Solution().asciiCode()
        assert answer_3 == expected_3

    with patch('builtins.input', side_effect=case_4):
        answer_4 = Solution().asciiCode()
        assert answer_4 == expected_4

    with patch('builtins.input', side_effect=case_5):
        answer_5 = Solution().asciiCode()
        assert answer_5 == expected_5

    with patch('builtins.input', side_effect=case_6):
        answer_6 = Solution().asciiCode()
        assert answer_6 == expected_6

