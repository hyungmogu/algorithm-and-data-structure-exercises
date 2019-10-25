# matrix spiral
#
# Given 2D array of integers, create an algorithm that travels in ccw and
# store its number s.th the output presents all numbers traveled in the matrix
# in ccw direction
#
# input
#   - 2d list of integers
# output
#   - 1d list of integers
#
#
#               v
# [[x, x, x, x, x ], x
#  [6, 7, 8, 9, x],
#  [11,12,13,14,x],
#  [x, x, x, x, x]]
#   ^
#
# [[x, x, x, x, x ],
#  [x, x, x, x, x ],
#  [x, x, x,x,x ],
#  [x, x,x,x,x ]] <
#
# Pseudocode
class Solution:
    def solve(self, matrix):
        #   1. initially travel in right direction
        direction = 'right'
        index_position = [0,0]
        output = []

        while not self.has_reached_the_end(matrix, index_position):
            #   2. check if obstacles exist
            if self.obstacles_exist(matrix, index_position, direction):

            #       2.1 if obstacles exist, change direction
                #           - 'right' --> 'down'
                #           - 'down' --> 'left'
                #           - 'left' --> 'up'
                #           - 'up' --> 'right'
                if direction == 'right':
                    direction = 'down'
                elif direction == 'down':
                    direction = 'left'
                elif direction == 'left':
                    direction = 'up'
                elif direction == 'up':
                    direction = 'right'

            #   3. pickup the number, and store inside 'output'
            number = matrix[index_position[0]][index_position[1]]
            output.append(number)

            #   4. replace the number in matrix with x
            matrix[index_position[0]][index_position[1]] = 'x'

            #   5. move in that direction
            self.move(index_position, direction)

        #   6. continue step 2 and 6 until it has reached the end
        number = matrix[index_position[0]][index_position[1]]
        output.append(number)

        return output
        # Time complexity is O(N^2), and sptial complexity O(N^2)

    def move(self, index_position, direction):
        if direction == 'right':
            index_position[1] += 1
        elif direction == 'down':
            index_position[0] += 1
        elif direction == 'left':
            index_position[1] -= 1
        elif direction == 'up':
            index_position[0] -= 1

    def obstacles_exist(self, matrix, index_position, direction):
        index_position_row = index_position[0]
        index_position_col = index_position[1]

        try:
            if (direction == 'right' and
                type(matrix[index_position_row][index_position_col + 1]) == int):

                return False

            if (direction == 'down' and
                type(matrix[index_position_row + 1][index_position_col]) == int):

                return False

            if (direction == 'left' and
                type(matrix[index_position_row][index_position_col - 1]) == int):

                return False

            if (direction == 'up' and
                type(matrix[index_position_row - 1][index_position_col]) == int):

                return False
        except IndexError:
            return True

        return True

    def has_reached_the_end(self, matrix, index_position):
        if (self.obstacles_exist(matrix, index_position, 'right') and
            self.obstacles_exist(matrix, index_position, 'down') and
            self.obstacles_exist(matrix, index_position, 'left') and
            self.obstacles_exist(matrix, index_position, 'up')):

            return True

        return False


if __name__ == '__main__':
    case_1 = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11,12,13,14,15],
              [16,17,18,19,20]]

    expected_1 = [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]

    solution_1 = Solution().solve(case_1)
    print(solution_1)

    assert expected_1 == solution_1