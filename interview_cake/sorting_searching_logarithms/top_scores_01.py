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
#
# Solution O(N) --> use fact that the highest score possible is 100
# 1. for each score, store freqency count in 'score_frequency'
# 2. counting backward from 100 to 0, add [score] * frequency to sorted_list
# 3. return output

class Solution:
    def highestScore(self, unsorted_scores, highest_possible_score):
        score_frequency = {}
        sorted_list = []

        for score in unsorted_scores:
            if score in score_frequency:
                score_frequency[score] += 1
            else:
                score_frequency[score] = 1

        for score in reversed(range(highest_possible_score + 1)):
            if score in score_frequency:
                frequency = score_frequency[score]
                sorted_list.extend([score] * frequency)

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