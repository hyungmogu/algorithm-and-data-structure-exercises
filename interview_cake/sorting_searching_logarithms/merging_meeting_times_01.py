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
# 1
# [(0, 1), (3, 5), (4, 8)]       []
#   x
#             ^
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
#    ^
#
# Can't be merged because 3 is not between 0 and 1
#
#
# 5
# [(0, 1), (3, 5), (4, 8)]       [(0,1), (3,8)]
#             x
#                            ^
#
# can be merged because 4 is not between 3 and 5
#
# Input
#   - list of tuples (of integers)
#
# output
#   - list of tuples (of integers)
#
# Cases
#   1. tuple is empty
#   2. there are no tuples that can be merged to one
#   3. there is at least two tuples that can be merged to one
#   4.
#
# Brute Force Solution -> O(N^2) --> We can do better!!
#
# Improved Solution
#   1. Sort elements in array by first element in tuple
#   2. for each element in schedules, starting at index == 1
#   2.1 if schedules[index][0] is in between schedules[index-1][0] and schedules[index-1][1], then append (schedules[index-1][0], max(schedules[index][1], schedules[index][0])) to merged_schedule
#   2.2 if not 2.1 append schedules[index-1] to merged_schedule
#   2.3 if not 2.1 and at the end of array, append schedules[index] to merged_schedule

#

class Solution:
    def mergeMeetingTimes(self, schedules):
        #   1. Sort elements in array by first element in tuple
        print('I am here')
        index = 1
        sorted_schedules = schedules.sort(key = lambda x: x[0])
        merged_schedule = []

        #   2. for each element in schedules, starting at index == 1
        while index < len(schedules):
            #   2.1 if schedules[index][0] is in between schedules[index-1][0] and schedules[index-1][1], then append (schedules[index-1][0], max(schedules[index][1], schedules[index][0])) to merged_schedule
            if schedules[index][0] >= schedules[index-1][0] and schedules[index][0] <= schedules[index-1][1]:
                merged_schedule.append((schedules[index-1][0], max(schedules[index-1][1], schedules[index][1])))

                index +=1
                continue

            #   2.2 if not 2.1 append schedules[index-1] to merged_schedule
            if schedules[index][0] > schedules[index-1][1]:
                merged_schedule.append(schedules[index-1])

            #   2.3 if not 2.1 and at the end of array, append schedules[index] to merged_schedule
            if schedules[index][0] > schedules[index-1][1] and index < len(schedules) - 1:
                merged_schedule.append(schedules[index])

            #
            index +=1

        return merged_schedule


solution_1 = Solution().mergeMeetingTimes([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
if __name__ == '__name__':
    case_1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    expected_1 = [(0, 1), (3, 8), (9, 12)]
    solution_1 = Solution().mergeMeetingTimes(case_1)
    assert expected_1 == solution_1