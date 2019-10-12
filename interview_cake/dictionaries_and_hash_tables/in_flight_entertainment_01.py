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
# Assume your users will watch exactly two movies
# Don't make your users watch the same movie twice
# Optimize for runtime over memory
#
# Brute force approach
#   1. for each movie length in movie_lengths, find the required length of second movie (flight_length - movie_lengths[index])
#   2. walk through the elements in movie lengths again
#   3. if not the same, check if sum equals movie total
#   4. if equal, then return True
#   5. else, return False

# the above has O(N^2) time complexity and O(1) spatial complexity

# we can do better
#   1. turn movie_lengths to sets
#   2. for each movie length in movie_lengths, find required length of second movie (flight_length - movie_lengths[index])
#   3. check set if the second movie exists
#   4. if exists, then return True
#   5. else, return False


# the improved solution has O(N) time complexity and O(N) spatial complexity

class Solution:
    def inFlightEntertainment(self, flight_length, movie_lengths):
        #   1. turn movie_lengths to sets
        movie_lengths_set = set(movie_lengths)

        #   2. for each movie length in movie_lengths, find required length of second movie (flight_length - movie_lengths[index])
        for first_movie_length in movie_lengths:
            second_movie_length = flight_length - first_movie_length

        #   3. check set if the second movie exists
        #   4. if exists, then return True
            if (second_movie_length in movie_lengths_set) and (second_movie_length != first_movie_length):
                return True

        # 5. otherwise, return False
        return False


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





