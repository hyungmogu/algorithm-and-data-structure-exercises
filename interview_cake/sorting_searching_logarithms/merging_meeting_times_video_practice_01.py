# Merging Meeting Times
#
#
# Your company built an in-house calendar tool called HiCal. You want to add a
# feature to see the times in a day when everyone is available.
#
# To do this, you’ll need to know when any team is having a meeting. In HiCal, a
# meeting is stored as a tuple ↴ of integers (start_time, end_time). These integers
# represent the number of 30-minute blocks past 9:00am.
#
# For example:
#
# (2, 3)  # Meeting from 10:00 – 10:30 am
# (6, 9)  # Meeting from 12:00 – 1:30 pm
#
# Write a function merge_ranges() that takes a list of multiple meeting time
# ranges and returns a list of condensed ranges.
#
# For example, given:
#
#   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#
# your function would return:
#
#   [(0, 1), (3, 8), (9, 12)]
#
# Do not assume the meetings are in order. The meeting times are coming from
# multiple teams.
#
# Write a solution that's efficient even when we can't put a nice upper bound on
# the numbers representing our time ranges. Here we've simplified our times down
# to the number of 30-minute slots past 9:00 am. But we want the function to work
# even for very large numbers, like Unix timestamps. In any case, the spirit of
# the challenge is to merge meetings where start_time and end_time don't have an
# upper bound.
#
# Input
#   - list of tuples
# Output
#   - list of tuples
#
# Constraints/known
#   - schedules in list is unsorted
#
# Brute Force
#
# 1
# [(0, 1), (3, 5), (4, 8)]       []
#    x
#    ^
#
# 2
# [(0, 1), (3, 5), (4, 8)]       []
#   x
#             ^
#
# Can't be merged because 3 is not between 0 and 1
#
# 3
# [(0, 1), (3, 5), (4, 8))]       []
#   x
#                      ^
#
# Can't be merged because 4 is not between 0 and 1
#
# 4
# [(0, 1), (3, 5), (4, 8)]       [(0,1)]
#             x
#                     ^
#
# Can't be merged because 3 is not between 0 and 1
#
#
# 5
# schedules = [(0, 1), (3, 5), (4, 8)]       [(0,1), (3,8)]
#                                        x
#                                        ^
#
# Brute force solution --> O(N^2), spatial complexity of O(N)
#
#
# Can we do better ? YES!!!  --> can be reduced to O(N*LOG N)
#
# [(0, 1), (3, 5), (4, 8)]  [(0,1)]
#            x
#
# is schedule[0] and schedule[1] mergeable ? NO --> append first element to solution
#
# [(0, 1), (3, 5), (4, 8)]  [(0,1), (3,8)]
#                           x
#
# is schedule[2] and schedule[1] mergeable ? YES --> merge two elements and put to arr
#
#
# Pseudocode
#   1. Sort schedules by the first element in tuple in increasing order
#   2. Starting at index of 1, check if schedules[0] is mergeable with schedules[1]
#   2.1 if mergeable, and is mergeable with last merged_schedules, set merged_schedules[-1] = (merged_schedules[-1][0], max(merged_schedules[-1][1], schedule[index][1]))
#   2.1 if mergeable, and not mergeable with last merged_schedules, append (schedule[index][0], max(schedule[index][1], schedule[index-1][1])) to 'merged_schedules'
#   2.2 if not mergeable, and schedules[index-1] is mergeable with last merged_schedules, append schedules[index] to 'merged_schedule'
#   2.3 if not mergeable, and index == 0, append schedules[index-1] to 'merged_schedules'
#
# Check pseudocode
# [(0, 1), (3, 5), (4, 6), (7, 8) (10, 12), (9, 10), (11, 12)]
#
# 1
# [(0, 1), (3, 5), (4, 6), (7, 8), (9, 10), (10, 12), (11, 12)]
#
# 2
# [(0, 1), (3, 5), (4, 6), (7, 8), (9, 10), (10, 12), (11, 12)] --> not mergeable --> [(0,1)]
#            x
#
# 3
# [(0, 1), (3, 5), (4, 6), (7, 8), (9, 10), (10, 12), (11, 12)] --> mergeable --> [(0,1), (3,6)]
#                    x
#
# 4
# [(0, 1), (3, 5), (4, 6), (7, 8), (9, 10), (10, 12), (11, 12)] --> not mergeable --> [(0,1), (3,6), (7,8)]
#                             x
# 5
# [(0, 1), (3, 5), (4, 6), (7, 8), (9, 10), (10, 12), (11, 12)] --> not mergeable --> [(0,1), (3,6), (7,8), (9, 10)]
#                                     x
#
# 6
# [(0, 1), (3, 5), (4, 6), (7, 8), (9, 10), (10, 12), (11, 12)] --> mergeable --> [(0,1), (3,6), (7,8), (9,12)]
#                                               x
#
# 7
# [(0, 1), (3, 5), (4, 6), (7, 8), (9, 10), (10, 12), (11, 12)] --> mergeable --> [(0,1), (3,6), (7,8), (9,12)]
#                                                         x
# cases
#
# 1. schedules is empty
# 2. there is only one schedule in 'schedules'
# 3. there is more than one schedules in 'schedules'
#   3.1 if two are not mergeables
#   [(0, 1), (3, 5)] --> if starting at index == 1, and not mergeable, then append schedules[0] to merged_schedules
#   [(3, 5), (7, 9)] --> if starting at index == 1, and not mergeable, then append schedules[1] to merged_schedules
#   [(3, 5), (7, 9), (11, 12)] --> if starting at index == 1 and not mergeable, then append schedules[0] to merged_schedules
#
#   3.2 if two are mergeables
#   [(0, 5), (3, 6)] --> [(0, 6)] (schedule[index][0], schedule[index][1])
#   [(0, 5), (2, 5)] --> [(0, 5)] (schedule[index][0], schedule[index][1])
#   [(0, 5), (5, 4)] --> [(0, 5)] (schedule[index][0], schedule[index-1][1])
#   (schedule[index][0], max(schedule[index][1], schedule[index-1][1]))
#
#   The question here is, starting from index == 1, how can we merge three toghter?

#   3.3 if two or more are mergeables
#   [(0, 5), (3, 6), (4, 8)] -> [(0, 8)]
#              x
# 1
#   [(0, 5), (3, 6), (4, 8)] -> [(0, 6)] --> [(0, 8)]
#                       x
#
#   (merged_schedules[-1][0], max(merged_schedules[-1][1], schedule[index][1]))
# if len(merged_schedules) > 0, check mergeability with schedules[index] and merged_shcedules[-1]
#
#
#
#
# Pseudocode
# def mergeMeetingTimes(self, schedules):
#     #   1. Sort schedules by the first element in tuple in increasing order
#     schedules = schedules.sort(key=lambda x: x[0])
#     merged_schedules = []
#     index = 1
#     #   2. Starting at index of 1, check if schedules[0] is mergeable with schedules[1]
#     while index < len(schedules):
#         #   2.1 if mergeable, and is mergeable with last merged_schedules, set merged_schedules[-1] = (merged_schedules[-1][0], max(merged_schedules[-1][1], schedule[index][1]))
#         if self.isMergeable(schedules[index-1], schedules[index]) and self.isMergeableWithLastMergedSchedule(merged_schedules, schedules[index]):
#             merged_schedules[-1] = (merged_schedules[-1][0], max(merged_schedules[-1][1], schedule[index][1]))
#             index += 1
#             continue

#         #   2.1 if mergeable, and not mergeable with last merged_schedules, append (schedule[index][0], max(schedule[index][1], schedule[index-1][1])) to 'merged_schedules'
#         if self.isMergeable(schedules[index-1], schedules[index]) and not self.isMergeableWithLastMergedSchedule(merged_schedules, schedules[index]):
#             merged_schedules.append((schedule[index][0], max(schedule[index][1], schedule[index-1][1])))
#             index += 1
#             continue

#         #   2.2 if not mergeable, and schedules[index-1] is mergeable with last merged_schedules, append schedules[index] to 'merged_schedule'
#         if not self.isMergeable(schedules[index-1], schedules[index]) and self.isMergeableWithLastMergedSchedule(merged_schedules, schedules[index-1]):
#             merged_schedules.append(schedules[index])
#             index += 1
#             continue

#         #   2.3 if not mergeable, and index == 0, append schedules[index-1] to 'merged_schedules'
#         if not self.isMergeable(schedules[index-1], schedules[index]) and index == 0:
#             merged_schedules.append(schedules[index-1])
#             index += 1
#             continue

#     return merged_schedules

# def isMergeable(self, schedule1, schedule2):
#     if schedule2[0] > schedule1[0] and schedule2[0] < schedule1[1]:
#         return True
#     return False

# def isMergeableWithLastMergedSchedule(merged_schedules, schedule):
#     if schedule[0] > merged_schedules[-1][0] and schedule[0] < merged_schedules[-1][1]:
#         return True
#     return False


class Solution:
    def mergeMeetingTimes(self, schedules):
        #   1. Sort schedules by the first element in tuple in increasing order
        schedules.sort(key=lambda x: x[0])
        merged_schedules = []
        index = 1
        #   2. Starting at index of 1, check if schedules[0] is mergeable with schedules[1]
        while index < len(schedules):

            print(index)
            #   2.1 if mergeable, and is mergeable with last merged_schedules, set merged_schedules[-1] = (merged_schedules[-1][0], max(merged_schedules[-1][1], schedule[index][1]))
            if self.isMergeable(schedules[index-1], schedules[index]) and self.isMergeableWithLastMergedSchedule(merged_schedules, schedules[index]):
                merged_schedules[-1] = (merged_schedules[-1][0], max(merged_schedules[-1][1], schedules[index][1]))
                index += 1
                continue

            #   2.1 if mergeable, and not mergeable with last merged_schedules, append (schedule[index][0], max(schedule[index][1], schedule[index-1][1])) to 'merged_schedules'
            if self.isMergeable(schedules[index-1], schedules[index]) and not self.isMergeableWithLastMergedSchedule(merged_schedules, schedules[index]):
                merged_schedules.append((schedules[index-1][0], max(schedules[index][1], schedules[index-1][1])))
                index += 1
                continue

            #   2.2 if not mergeable, and schedules[index-1] is mergeable with last merged_schedules, append schedules[index] to 'merged_schedule'
            if not self.isMergeable(schedules[index-1], schedules[index]) and self.isMergeableWithLastMergedSchedule(merged_schedules, schedules[index-1]):
                merged_schedules.append(schedules[index])
                index += 1
                continue

            #   2.3 if not mergeable, and index == 0, append schedules[index-1] to 'merged_schedules'
            if not self.isMergeable(schedules[index-1], schedules[index]) and index == 1:
                merged_schedules.append(schedules[index-1])
                index += 1
                continue

        return merged_schedules

    def isMergeable(self, schedule1, schedule2):
        if schedule2[0] >= schedule1[0] and schedule2[0] <= schedule1[1]:
            return True
        return False

    def isMergeableWithLastMergedSchedule(self, merged_schedules, schedule):
        if len(merged_schedules) == 0:
            return False

        if schedule[0] >= merged_schedules[-1][0] and schedule[0] <= merged_schedules[-1][1]:
            return True
        return False

if __name__ == '__main__':
    case_1 = [(0, 1), (3, 5), (4, 6), (7, 8), (9, 10), (10, 12), (11, 12)]
    expected_1 = [(0,1), (3,6), (7,8), (9,12)]
    solution_1 = Solution().mergeMeetingTimes(case_1)
    print(solution_1)
    assert expected_1 == solution_1