# Top scores (Repeat problem from Sorting and Searching)
# https://www.interviewcake.com/question/python/top-scores?course=fc1&section=hashing-and-hash-tables
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
# 1
#
# [37, 89, 41, 65, 91, 65]
#  x
# {37: 1}
#
# 2
#
# [37, 89, 41, 65, 91, 65]
#       x
# {37: 1, 89: 1}
#
#
# 2
#
# [37, 89, 41, 65, 91, 65]
#          x
# {37: 1, 89: 1, 41: 1}
#
# 3
#
# [37, 89, 41, 65, 91, 65]
#               x
# {37: 1, 89: 1, 41: 1, 65: 1}
#
#
# 4
#
# [37, 89, 41, 65, 91, 65]
#                  x
# {37: 1, 89: 1, 41: 1, 65: 1, 91: 1}
#
# 5
#
# [37, 89, 41, 65, 91, 65]
#                       x
# {37: 1, 89: 1, 41: 1, 65: 2, 91: 1}
#
# 6
#
# iterate [100 ... 0] backward and check dictionary
#
# [91, 89, 65, 65, 41, 37]
#
# O(100 * N) --> O(100N) --> O(N)
#
# Pseudocode
# def highestScore(self, unsorted_scores, highest_possible_score):
#     #   1. count the frequency of numbers in 'unsorted_scores', and store in 'word_frequency'
#     HIGHEST_SCORE = 100
#     sorted_scores =[]
#     word_frequency = {}
#     index_score = HIGHEST_SCORE

#     for score in unsorted_scores:
#         if score in word_frequency:
#             word_frequency[score] += 1
#         else:
#             word_frequency[score] = 1

#     #   2. iterating index backward from 100 to 0
#     while index_score > 0:
#         #   2.1 if index in 'word_frequency', append index word_frequency[index] many times to 'sorted_scores'
#         if index_score in word_frequency:
#             sorted_scores.extend([index_score for x in range(word_frequency[index_score])])

#         index_score -= 1
#     #   3. return sorted_scores

#     return sorted_scores
    #
# [91, 89, 65, 53, 41, 37]
#

class Solution:
    def highestScore(self, unsorted_scores, highest_possible_score):
        #   1. count the frequency of numbers in 'unsorted_scores', and store in 'word_frequency'
        HIGHEST_SCORE = 100
        sorted_scores =[]
        word_frequency = {}
        index_score = HIGHEST_SCORE

        for score in unsorted_scores:
            if score in word_frequency:
                word_frequency[score] += 1
            else:
                word_frequency[score] = 1

        #   2. iterating index backward from 100 to 0
        while index_score > 0:
            #   2.1 if index in 'word_frequency', append index word_frequency[index] many times to 'sorted_scores'
            if index_score in word_frequency:
                sorted_scores.extend([index_score for x in range(word_frequency[index_score])])

            index_score -= 1
        #   3. return sorted_scores

        return sorted_scores


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