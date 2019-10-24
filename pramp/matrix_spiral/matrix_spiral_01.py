# matrix spiral
#
# goal: given 2d array of integers, create an algorithm that walks over the
# matrix in a spiral manner in ccw direction. also, generate a list that shows
# all of the traveled elements
#
#
# [[x, 2, 3, 4, 5],
#  [6, 7, 8, 9, 10],
#  [11,12,13,14,15],
#  [16,17,18,19,20]]
#
# [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]
#
#
# input: array.array of integers
# output: array of integers
# 1. move in right direction while checking for obstacle
# 2. if obstacle is found, and path exists below, then change direction to downward
# 3. move in down direction while checking for obstacle
# 4. if obstacle is found, and path exists to left, then change direction to left
# 5. move in left direction while checking for obstacle
# 6. if obstacle is found, and path exists upward, then change direction upward


class Solution:
    def solve(self, matrix):
        direction = 'right'
        index_position = [0, 0]
        output = []

        while not self.reached_the_end(index_position, matrix):
            # 1. move in right direction while checking for obstacle
            # 2. if obstacle is found, and path exists below, then change direction to downward
            # 3. move in down direction while checking for obstacle
            # 4. if obstacle is found, and path exists to left, then change direction to left
            # 5. move in left direction while checking for obstacle
            # 6. if obstacle is found, and path exists upward, then change direction upward

            self.move(matrix, index_position, direction, output)

            if self.obstacle_exists(matrix, index_position, direction):
                if direction == 'right':
                    direction = 'down'

                elif direction == 'down':
                    direction = 'left'

                elif direction == 'left':
                    direction = 'up'

                elif direction == 'up':
                    direction = 'right'

        # 7. Add the last element!
        output.append(matrix[index_position[0]][index_position[1]])

        return output

    def reached_the_end(self, index_position, matrix):
        if (self.obstacle_exists(matrix, index_position, 'right') and
            self.obstacle_exists(matrix, index_position, 'down') and
            self.obstacle_exists(matrix, index_position, 'left') and
            self.obstacle_exists(matrix, index_position, 'up')):
            return True

        return False

    def obstacle_exists(self, matrix, index_position, direction):
        index_position_row = index_position[0]
        index_position_col = index_position[1]
        try:
            if (direction == 'right' and
                matrix[index_position_row][index_position_col + 1] == 'x'):
                return True

            if (direction == 'down' and
                matrix[index_position_row + 1][index_position_col] == 'x'):
                return True

            if (direction == 'left' and
                matrix[index_position_row][index_position_col - 1] == 'x'):
                return True

            if (direction == 'up' and
                matrix[index_position_row - 1][index_position_col] == 'x'):
                return True
        except IndexError:
            return True

        return False

    def move(self, matrix, index_position, direction, output):
        index_position_row = index_position[0]
        index_position_col = index_position[1]

        output.append(matrix[index_position_row][index_position_col])
        matrix[index_position_row][index_position_col] = 'x'
        if direction == 'right':
            index_position[1] += 1

        elif direction == 'down':
            index_position[0] += 1

        elif direction == 'left':
            index_position[1] -= 1

        elif direction == 'up':
            index_position[0] -= 1


if __name__ == '__main__':
    case_1 = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11,12,13,14,15],
              [16,17,18,19,20]]

    expected_1 = [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]

    solution_1 = Solution().solve(case_1)
    assert expected_1 == solution_1