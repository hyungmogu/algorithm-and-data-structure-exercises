# 스택
#
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#
# 명령은 총 다섯 가지이다.
#
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다. []
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
#
# Example 1 (예 입력)
# 14
# push 1
# push 2 <- [1, 2]
# top <- 2
# size <- 2
# empty <- 0
# pop <- 2 [1]
# pop <- 1 []
# pop <- -1
# size <- 0
# empty <- 1
# pop <- -1
# push 3 <- [3]
# empty <- 0
# top <- 3
#
#
# 예 출력
# 2
# 2
# 0
# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3

from unittest.mock import patch

# outline program (stack 메소드)
class Solution:
    def __init__(self):
        self.items = []

    def stack(self):
        # pseudocode (stack)
        #   1. 인풋 (input)을 통해 입력정보를 받는다. 그리고 변수 'size' 그리고 'commands'에 저장한다
        inputs = self.getInput()
        size = int(inputs[0])
        commands = [x.split() for x in inputs[1:]]

        output = []

        #   2. for문을 사용해 각 명령을 메소드로 실행한다
        for command in commands:
            if command[0] == 'push':
                self.push(int(command[1]))

            if command[0] == 'pop':
                popped_value = self.pop()
                output.append(popped_value)

            if command[0] == 'size':
                size_value = self.size()
                output.append(size_value)

            if command[0] == 'empty':
                empty_value = self.empty()
                output.append(empty_value)

            if command[0] == 'top':
                top_value = self.top()
                output.append(top_value)

        return output

    def push(self, val):
        # 정수 X를 스택에 넣는 연산이다.
        #   1. 배열 'self.items'의 append를 통해 정수를 삽입한다
        self.items.append(val)

    def pop(self):
        # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        #   1. 정수가 self.items 에 없을때 -1을 출력한다
        if len(self.items) == 0:
            return -1

        #   2.  배열 'self.items'의 pop을 통해 마지막 정수를 빼고, 변수 popped_value에 저장하고 정수를 리턴한다
        return self.items.pop()

    def size(self):
        # 스택에 들어있는 정수의 개수를 출력한다.
        #   1. len 함수를 이용해 개수를 리턴한다
        return len(self.items)

    def empty(self):
        # 스택이 비어있으면 1, 아니면 0을 출력한다
        #   1. len 함수를 이용해 개수 정보를 얻는다
        #   2. 개수가 0 이면 1를 리턴한다
        if len(self.items) == 0:
            return 1

        #   3. 개수가 0 이상이면 0를 리턴한다
        return 0

    def top(self):
        # 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        #   1. len 함수를 이용해 개수 정보를 얻는다
        #   2. 개수가 0 이면 -1를 리턴한다
        if len(self.items) == 0:
            return -1

        #   3. 개수가 0 이상이면 self.items[-1]를 리턴한다
        return self.items[-1]

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
        '14',
        'push 1',
        'push 2',
        'top',
        'size',
        'empty',
        'pop',
        'pop',
        'pop',
        'size',
        'empty',
        'pop',
        'push 3',
        'empty',
        'top'
    ]

    case_2 = [
        '7',
        'pop',
        'top',
        'push 123',
        'top',
        'pop',
        'top',
        'pop'
    ]

    expected_1 = [ 2, 2, 0, 2, 1, -1, 0, 1, -1, 0, 3]
    expected_2 = [-1, -1, 123, 123, -1, -1]

    with patch('builtins.input', side_effect=case_1):
        answer_1 = Solution().stack()
        print(answer_1)
        assert answer_1 == expected_1

    with patch('builtins.input', side_effect=case_2):
        answer_2 = Solution().stack()
        print(answer_2)
        assert answer_2 == expected_2



