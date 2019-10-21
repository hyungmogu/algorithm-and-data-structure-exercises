# Drone Flight Planner
#
# create a function calc_drone_min_energy that computes and returns the
# mininimal amount of energy the drone would need to complete its route.
# Assume that the drone starts its flight at the first point in route.

# Constraints
# input -> array.array.integer (1 <= route.length <= 100)
# output -> integer

# input -> [[1,2,3],[4,5,6],[7,8,9]]
# calDroneMinEnergy(input) -> 6

# input -> [[1,2,6],[3,4,3],[2,4,1]]
# calDonreMinEnergy(input) -> 0

# known
#  - ascending -> 1kwh
#  - descending -> -1kwh
#  z point is the point that matters

# solve(example_input) = 6
# solve(input2) = 0

# Pseudocode
class Solution:
    def solve(self, paths): # paths --> 매개변수
        #   1. 전달인자를 'flight_paths'에 저장한다
        #   2. 높이의 기초값을 구한다
        max_height = 0
        initial_height = paths[0][2]

        #   3. for문을 이용해 current_height - initial_height 로 순 높이를 구한다. 그리고 그 값을 'net_height'에 저장한다
        for point in paths:
            current_height = point[2]
            net_height = current_height - initial_height
            #   4. if문을 이용해 max_height < net_height, set max_height = net_height

            if max_height < net_height:
                max_height = net_height

        #   5. max_height을 리턴한다
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

