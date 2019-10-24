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


def solve(self, matrix):
    direction = 'right'
    index_position = [0, 0]

    while not self.reached_the_end(index_position, matrix):
        # 1. move in right direction while checking for obstacle
        # 2. if obstacle is found, and path exists below, then change direction to downward
        # 3. move in down direction while checking for obstacle
        # 4. if obstacle is found, and path exists to left, then change direction to left
        # 5. move in left direction while checking for obstacle
        # 6. if obstacle is found, and path exists upward, then change direction upward

        if self.obstacle_exists(matrix, index_position, direction):
            if direction == 'right':
                direction = 'down'

            if direction == 'down':
                direction = 'left'

            if direction == 'left':
                direction = 'up'

            if direction == 'up':
                direction = 'right'

        self.move(matrix, index_position, direction)

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
            matrix[index_postion_row + 1][index_position_col] == 'x'):
            return True

        if (direction == 'left' and
            index_position_col == 0 or
            matrix[index_position_row][index_position_col - 1] == 'x'):
            return True

        if (direction == 'up' and
            index_position_row == -1 or
            matrix[index_position_row - 1][index_position_col] == 'x'):
            return True
    except IndexError:
        return True

    return False

def move(self, matrix, index_position, direction):



class Solution:
    def solve(self, matrix)


if __name__ == '__main__':
    case_1 = [[x, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11,12,13,14,15],
              [16,17,18,19,20]]

    expected_1 = [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]

