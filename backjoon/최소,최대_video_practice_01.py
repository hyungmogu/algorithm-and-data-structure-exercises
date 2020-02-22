"""
Note: Incomplete. Hyungmo fell asleep.
Solution addressed in 최소,최대_video_practice_02.py
"""

# 최소, 최대
# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
#
# 예제 입력 1

# 5
# 20 10 35 30 7

#
# 예제 출력 1
# 7 35

# pseudocode
# 1. input을 통해 배열 사이즈 n 그리고 정수 배열 입력 정보를 받는다. 그리고 그 정보를 변수 'n' 그리고 'numbers'안에 저장한다
#     contents = self.getInput()
#     n = int(contents[0])
#     numbers = [int(x) for x in contents[1].split()]

# # 2. maximum 값 그리고 minimum 값을 구한다
    index_maximum = 0
    index_minimum = 0

    maximum = None
    minmum = None
    while index_maximum < len(numbers):
        if index == 0:
            maximum = numbers[index_maximum]
            index += 1
            continue

        if numbers[index_maximum] > maximum:
            maximum = numbers[index_maximum]
        else:

#         index += 1

#     minmum = None
#     while minmum < len(numbers):
#         if index == 0:
#             maximum = numbers[minmum]
#             index += 1
#             continue

#         if numbers[index_minimum] > minmum:
#             minmum = numbers[index_maximum]
#         else:

#         index += 1

# # 3. maximum 그리고 minimum 값을 return 한다
#     return '{} {}'.format(minimum, maximum)






class Solution:
    def solve(self):
        contents = self.getInput()
        n = int(contents[0])
        numbers = [int(x) for x in contents[1].split()]

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
    case_1 = [
        '5',
        '20 10 35 30 7'
    ]

    expected_1 = '7 35'

    with patch('builtins.input', side_effect=case_1):
        answer_1 = Solution().solve()

        assert answer_1 == expected_1