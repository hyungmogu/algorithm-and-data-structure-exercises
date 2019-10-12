# Top scores
#
# You created a game that is more popular than Angry Birds.
#
# Each round, players receive a score between 0 and 100, which you use to rank
# them from highest to lowest. So far you're using an algorithm that sorts in
# O(nlgn) time, but players are complaining that their rankings aren't updated
# fast enough. You need a faster sorting algorithm.
#
# Write a function that takes:
#
# a list of unsorted_scores
# the highest_possible_score in the game
# and returns a sorted list of scores in less than O(nlgn) time.
#
# For example:
#
# unsorted_scores = [37, 89, 41, 65, 91, 53]
# HIGHEST_POSSIBLE_SCORE = 100
#
# Returns [91, 89, 65, 53, 41, 37]
# sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
#
# We’re defining n as the number of unsorted_scores because we’re expecting the
# number of players to keep climbing.
#
# And, we'll treat highest_possible_score as a constant instead of factoring it
# into our big O time and space costs because the highest possible score isn’t
# going to change. Even if we do redesign the game a little, the scores will
# stay around the same order of magnitude.
#
# Input
#   - list of integers
# Output
#   - integer
#
# contraint
#   - time complexity has to be less than O(nlgn)
#   - spatial complexity is ok

# [37, 37, 89, 41, 65, 91, 53]
#
# score_frequency = {37: 2, 89: 1, 41: 1, 65: 1, 91: 1, 53: 1}
#
# [100 ... 0]
#   --> does 100 exist ? NO => continue
#   ...
#   --> does 91 exiset ? YES => append 91 to list 'sorted_list'
#   ...
#   --> does 37 exist ? YES => extend([37] * 2) to list sorted_list

# return sorted_list

# Solution (O(N) time complexity!!)
#   1. count frequency for each element in unsorted_scores
#     score_frequency = {}

#     for score in unsorted_scores:
#         if score in score_freqency:
#             score_frequency[score] += 1
#         else:
#             score_frequency[score] = 1

# #   2. for each score from 100 to 0,
# #   2.1 if score exists in score_frequency, extend ([score] * frequency) to sorted_list
#     for score in reversed(range(highest_possible_score + 1)):
#         if score in score_frequency:
#             frequency = score_frequency[score]
#             sorted_list.extend([score] * frequency)


# #   3. return sorted_list
#     return sorted_list


class Solution:
    def highestScore(self, unsorted_scores, highest_possible_score):

        # Solution (O(N) time complexity!!)
        #   1. count frequency for each element in unsorted_scores
        score_frequency = {}
        sorted_list = []

        if len(unsorted_scores) == 0:
            return sorted_list

        for score in unsorted_scores:
            if score in score_frequency:
                score_frequency[score] += 1
            else:
                score_frequency[score] = 1

        #   2. for each score from 100 to 0,
        #   2.1 if score exists in score_frequency, extend ([score] * frequency) to sorted_list
        for score in reversed(range(highest_possible_score + 1)):
            if score in score_frequency:
                frequency = score_frequency[score]
                sorted_list.extend([score] * frequency)

        #   3. return sorted_list
        return sorted_list


if __name__ == '__main__':
    unsorted_scores_case_1 = [37, 89, 41, 65, 91, 53]
    unsorted_scores_case_2 = [37, 37, 89, 41, 65, 65, 91, 53]
    unsorted_scores_case_3 = []

    highest_possible_score_case_1 = 100
    highest_possible_score_case_2 = 100
    highest_possible_score_case_3 = 100

    expected_1 = [91, 89, 65, 53, 41, 37]
    expected_2 = [91, 89, 65, 65, 53, 41, 37, 37]
    expected_3 = []

    solution_1 = Solution().highestScore(unsorted_scores_case_1, highest_possible_score_case_1)
    solution_2 = Solution().highestScore(unsorted_scores_case_2, highest_possible_score_case_2)
    solution_3 = Solution().highestScore(unsorted_scores_case_3, highest_possible_score_case_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3