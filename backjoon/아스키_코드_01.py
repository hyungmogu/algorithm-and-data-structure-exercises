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
#   - 입력 total character count 는 1 이다
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
# 2개의 clarification questions
# 1. built-in 아스키-문자 함수를 써도되는가 *
# 2. built-in 함수를 쓰지않고 알고리즘을 만들어야 하는가
#
# 파이톤은 문자-아스키, 아스키-문자 변환 함수를 갖고 있습니다
#   1. chr (ascii -> character)
#   2. ord (character -> ascii) *
#
# pseudocode
    # #   1. 문자를 input 함수를 이용해 입력을 받는다. 그리고 입력 정보를 변수 'character' 에 저장한다
    # character = input()

    # #   2. char 함수를 이용해 문자를 아스카로 변환한다
    # character_ascii = char(character)

    # #   3. 변환된 아스키를 return으로 출력한다
    # return character_ascii


# 추축 -> time complexity O(1), spatial complexity O(N)

class Solution:
    def asciiCode(self, character):
        #   1. 문자를 input 함수를 이용해 입력을 받는다. 그리고 입력 정보를 변수 'character' 에 저장한다

        #   2. char 함수를 이용해 문자를 아스카로 변환한다
        character_ascii = ord(character)

        #   3. 변환된 아스키를 return으로 출력한다
        return character_ascii

    def getInput(self):
        contents = []
        while True:
            try:
                line = input()
            except Exception:
                break
            contents.append(line)

        return contents


if __name__ == '__main__':
    case_1 = 'A'
    case_2 = 'C'
    case_3 = '0'
    case_4 = '9'
    case_5 = 'a'
    case_6 = 'z'

    expected_1 = 65
    expected_2 = 67
    expected_3 = 48
    expected_4 = 57
    expected_5 = 97
    expected_6 = 122

    solution_1 = Solution().asciiCode(case_1)
    solution_2 = Solution().asciiCode(case_2)
    solution_3 = Solution().asciiCode(case_3)
    solution_4 = Solution().asciiCode(case_4)
    solution_5 = Solution().asciiCode(case_5)
    solution_6 = Solution().asciiCode(case_6)


