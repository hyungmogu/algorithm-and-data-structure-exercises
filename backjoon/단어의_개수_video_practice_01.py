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
# 'The Curious Case of Benjamin Button'
#
# 예제 출력 1
# 6
#
# 예제 입력 2
# '       '
#
# 예제 출력 2
# 0
#
# Pseudocode

from unittest.mock import patch

class Solution:
    def numberOfWords(self):
        #   1. input() 이용해 입력정보를 받는다 그리고 그 정보를 변수 'words' 에 저장한다
        words = input()

        #   2. 앞 뒤에 있는 공백들을 도려낸다
        words = words.strip()

        #   3. 띄어쓰기를 중심으로 단어들을 잘라낸다. 잘라낸 단어들을 배열 'words_list' 에 저장한다
        words_list = words.split()

        #   4. 파이톤 함수 len 을 이용해 단어의 갯수 값을 알아낸다. 그리고 그 값을 출력한다.
        return len(words_list)


if __name__ == '__main__':
    case_1 = [
        'The Curious Case of Benjamin Button'
    ]

    case_2 = [
        "Mazatneunde Wae Teullyeoyo"
    ]

    case_3 = [
        '       '
    ]

    expected_1 = 6
    expected_2 = 3
    expected_3 = 0

    with patch('builtins.input', side_effect=case_1):
        answer_1 = Solution().numberOfWords()
        print(answer_1)
        assert answer_1 == expected_1

    with patch('builtins.input', side_effect=case_2):
        answer_2 = Solution().numberOfWords()
        print(answer_2)
        assert answer_2 == expected_2

    with patch('builtins.input', side_effect=case_3):
        answer_3 = Solution().numberOfWords()
        print(answer_3)
        assert answer_3 == expected_3

