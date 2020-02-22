# Drone Flight Planner
#
# 함수 calc_drone_min_energy 를 구축해서 드론에게 필요한 최소 애너지 갚을 리턴하시오.
# 최소 애너지 값은 높이에만 적용된다 (1 pt 차 in z-axis = 1 애너지)
#
# 예문
#
#                     도착지점
#                       v
#   [[1,2,3],[4,5,6],[7,8,9]]
#       ^
#     출발지점
#
#  필요 애너지 9 - 3 = 6
#
# [[1,2,6],[3,4,3],[2,4,1]]
#
# 필요애너지 = 0 --> 왜? 드론이 내려가기 때문
#
# 입력
#   - 2D 배열
#
# 출력
#   - 정수

# Pseudocode
class Solution:
    def solve(self, paths): # paths --> 매개변수

        #   1. 출발지점 높이 값을 변수 'initial_height'에 저장한다
        initial_height = paths[0][2]
        max_height = 0

        #   2. for문을 이용해서 각 point의 순 높이 갚을 구한다 (net_height = current_height - initial_height)
        for point in paths:
            current_height = point[2]
            net_height = current_height - initial_height

            #   2.1. if문을 이용해서 max_height와 비교한다. max_height < net_height, set max_height = net_height
            if max_height < net_height:
                max_height = net_height

        #   3. max_height을 리던한다
        return max_height

if __name__ == '__main__':
    case_1 = [[1,2,3],[4,5,6],[7,8,9]]
    case_2 = [[1,2,6],[3,4,3],[2,4,1]]

    expected_1 = 6
    expected_2 = 0

    solution_1 = Solution().solve(case_1)
    solution_2 = Solution().solve(case_2)

    assert expected_1 == solution_1
    assert expected_2 == solution_2

