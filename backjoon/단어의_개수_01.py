# 단어의 개수
#
# 영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를
# 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
#
# 입력
# 첫 줄에 영어 대소문자와 띄어쓰기로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지
# 않는다. 단어는 띄어쓰기 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열의 앞과
# 뒤에는 공백이 있을 수도 있다.
#
# constraint
#   - 공백이 연속해서 나오는 경우는 없다
#   - 문자열의 앞과 뒤에는 공백이 있을 수도 있다.
#   - 단어는 띄어쓰기 한 개로 구분된다
#
# 출력
# 첫째 줄에 단어의 개수를 출력한다.
#
# 예제 입력 1
# The Curious Case of Benjamin Button
#
# 예제 출력 1
# 6
#
# Stack
#
# pseudocode
#   1. 문자열의 split()을 이용해 띄어쓰기 한개를 기준으로 문자열의 단어들을 나누어 배열 'words'에 채운다
#   2. len() 함수를 이용해 배열 사이즈를 얻는다
#   3 배열 사이즈를 출력한다

from unittest.mock import patch

class Solution:
    def numberOfWords(self):
        #   1. 문자열의 split()을 이용해 띄어쓰기 한개를 기준으로 문자열의 단어들을 나누어 배열 'words'에 채운다
        #   2. len() 함수를 이용해 배열 사이즈를 얻는다
        sentence = (self.getInput())[0]
        words = sentence.split()
        #   3 배열 사이즈를 출력한다
        return len(words)

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
    case_1 = [
        'The Curious Case of Benjamin Button'
    ]

    case_2 = [
        "Mazatneunde Wae Teullyeoyo"
    ]

    expected_1 = 6
    expected_2 = 3

    with patch('builtins.input', side_effect=case_1):
        answer_1 = Solution().numberOfWords()
        print(answer_1)
        assert answer_1 == expected_1

    with patch('builtins.input', side_effect=case_2):
        answer_2 = Solution().numberOfWords()
        print(answer_2)
        assert answer_2 == expected_2

