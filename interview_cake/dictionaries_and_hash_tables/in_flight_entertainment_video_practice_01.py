#In flight entertainment
#
# You've built an inflight entertainment system with on-demand movie streaming.
#
# Users on longer flights like to start a second movie right when their first
# one ends, but they complain that the plane usually lands before they can see
# the ending. So you're building a feature for choosing two movies whose total
# runtimes will equal the exact flight length.
#
# Write a function that takes an integer flight_length (in minutes) and a list
# of integers movie_lengths (in minutes) and returns a boolean indicating whether
# there are two numbers in movie_lengths whose sum equals flight_length.
#
# When building your function:
#
# 1. Assume your users will watch exactly two movies
# 2. Don't make your users watch the same movie twice
# 3. Optimize for runtime over memory <--
#
# Input
#   1. integer (movie length)
#   2. list of integers (various movie lengths in movies in minutes)
#
# output
#   1. boolean (True if the second movie exists, and false if not)

# Brute force solution
#   1. For each first_movie_length in movie_lengths
#   2. calculate the second_movie_length (flight_length - first_movie_length)
#   3. if first_movie_length == second_movie_length, continue
#   4. for each movie_length in movie_lengths, if movie_length == second_movie_length, return True
#   5. return False

# Example 1
# flight_length = 70
# movie_lengths = [10,20,30,40,50]
#                               x
#
# Returns True
#
#
# if first movie is 10
# second_moivie = 60
#
# Time Complexity O(N^2), spatial complexity O(1)

# Can we do better?
# Answer: YES!!!
#   - using sets
#       - it has O(1) look up time --> reduces to O(N)

#   1. For each first_movie_length in movie_lengths
#   2. calculate the second_movie_length (flight_length - first_movie_length)
#   3. if first_movie_length == second_movie_length, continue
#   4. if second_movie_length is in movie_lengths_set, return True
#   5. return False


class Solution:
    def inFlightEntertainment(self, flight_length, movie_lengths):
        movie_lengths_set = set(movie_lengths)

        #   1. For each first_movie_length in movie_lengths
        for first_movie_length in movie_lengths:
            #   2. calculate the second_movie_length (flight_length - first_movie_length)
            second_movie_length = flight_length - first_movie_length

            #   3. if first_movie_length == second_movie_length, return False
            if first_movie_length == second_movie_length:
                continue

            #   4. if second_movie_length is in movie_lengths_set, return True
            if second_movie_length in movie_lengths_set:
                return True

        return False
        #   5. return False


if __name__ == '__main__':
    flight_length_case_1 = 120
    movie_lengths_case1 = [10,20,30,40,50,60]

    flight_length_case_2 = 70
    movie_lengths_case2 = [10,20,30,40,50,60]

    expected_case_1 = False
    expected_case_2 = True

    solution_case_1 = Solution().inFlightEntertainment(flight_length_case_1, movie_lengths_case1)
    solution_case_2 = Solution().inFlightEntertainment(flight_length_case_2, movie_lengths_case2)

    assert expected_case_1 == solution_case_1
    assert expected_case_2 == solution_case_2


