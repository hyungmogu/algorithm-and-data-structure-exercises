# 수 정렬하기
#
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이
# 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
#
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
#
# constraints
#   - 배열의 개수는 최소 1개 이상이며 그리고 1000개 이하이다
#   - 배열 안에 있는 정수는 절대갑이 1,000 보다 작거나 같은 점수이다.
#   - 수는 중복되지 않는다
#
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
#
# 예제 입력 1
# 5
# 2
# 3
# 4
# 1
#
# 예제 출력 1
# 1
# 2
# 3
# 4
# 5
#
# [1,2,3,4,5]
#
#
#
# ^
# 5 4 3 2 1  -> [1,4,3,2,5]
#   *
#
#   ^
# 1 4 3 2 5  -> [1,2,3,4,5]
#       *
#
#     ^
# 1 2 3 4 5  -> [1,2,3,4,5]
#       *
#
#       ^
# 1 2 3 4 5  -> [1,2,3,4,5]
#         *
#
# time complexity of O(N^2), spatial complexity O(N)
#
#   - 더 개선할 수 있는가 ? 예스!!! O(N*LOG N)
#   -
#
# 5 4 3 2 1
#
#
#
#
# pseudocode
# outer loop --> index_i
# index of nested loop --> index_j
#
#   1. for each index_i with index_j == index_J + 1, 배열 nums[index+1:] 안에 가장 작은 정수를 찾는다. 이 인덱스를 index_minimum 에 저장한다.
    # index_i = 0

    # while index_i < len(nums) - 1:
    #     index_j = index_i + 1
    #     index_minimum = None
    #     minimum = None

    #     while index_j < len(nums):
    #         if index_j == index_i + 1:
    #             index_minimum = index_j
    #             minimum = nums[index_j]

    #         if index_j > index_i + 1 and nums[index_j] < minimum:
    #             minimum = nums[index_j]

    #         index_j += 1


    #     #   2. 정수[index_minimum] 그리고 정수[index_i] 하고 비교한다. 만약 정수[index_i] > 정수[index_minimum],  정수[index_minimum] 하고 정수[index_i]를 swap 한다
    #     if minimum < nums[index_j]:
    #         nums[index_j], minimum = minimum, nums[index_j]

    #     index_i += 1

    # return nums

#   3. index_i를 increment 한다
#
#   4. while 문을 index_i < len(nums) - 1 까지 실행한다
#
#   5. 정렬된 배열을 출력한다
#
#
#
#   1.
#
#

from unittest.mock import patch

class Solution:
    def sortInAscendingOrder(self):
        nums = [int(x) for x in self.getInput()]

        index_i = 0

        while index_i < len(nums) - 1:
            index_j = index_i + 1
            index_minimum = None
            minimum = None


            while index_j < len(nums):
                if index_j == index_i + 1:
                    index_minimum = index_j
                    minimum = nums[index_j]

                if index_j > index_i + 1 and nums[index_j] < minimum:
                    minimum = nums[index_j]
                    index_minimum = index_j

                index_j += 1


            #   2. 정수[index_minimum] 그리고 정수[index_i] 하고 비교한다. 만약 정수[index_i] > 정수[index_minimum],  정수[index_minimum] 하고 정수[index_i]를 swap 한다
            if minimum < nums[index_i]:
                nums[index_i], nums[index_minimum] = nums[index_minimum], nums[index_i]

            index_i += 1

        return nums

    def getInput(self):
        contents = []
        while True:
            try:
                line = input()
            except Exception:
                break
            contents.append(line)

        return contents




if __name__ == "__main__":
    case_1 = [
        5,
        4,
        3,
        2,
        1
    ]

    expected = [1,2,3,4,5]

    with patch('builtins.input', side_effect=case_1):
        answer = Solution().sortInAscendingOrder()
        print(answer)
        assert answer == expected

