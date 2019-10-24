# Time Planner
#   given two schedules in the form of list where each element is in the form
# [start_time, end_time], find overlapping schedules between two time slots
# that satisfies the duration requirement
#
#
# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#                                x
#         slotsB = [[0, 15], [60, 70]]
#                                x
#         duration = 8
#
# output: [60, 68]
#
#
#
# input
#   - 2D array with each element being list of integers * 2
#
# output
#   - list of integers
#
# constraint
#   - each schedules are ordered by start time
#   - if there is no solution, return empty array
#   - there is at least 1 schedule in each each time slot
#
# cases
#   1. general case
#       1.1  solution is satisfied
#       1.2 solution is not satisfied but overlaps partially
#       1.3 solution is not satisfied and they don't overlap
#
#
#
#
# pseudocode
class Solution:
    def solve(self, slot_a, slot_b, duration):
        #   1. initialize index_a and index_b to have value 0
        index_a = 0
        index_b = 0

        #   2. while index_a < len(slot_a) and index_b < len(slot_b):
        while index_a < len(slot_a) and index_b < len(slot_b):

            #       2.1 find the overlap
            start_time = max(slot_a[index_a][0], slot_b[index_b][0])
            end_time = min(slot_a[index_a][1], slot_b[index_b][1])

            overlap = end_time - start_time

            #       2.2 if satisfies the solution (overlap > duration), return [start_time, start_time + duration]
            if overlap > duration:
                return [start_time, start_time + duration]

            #       2.3 if solution is not satisfied
            if self.slot_a_is_earlier(slot_a, index_a, slot_b, index_b):
                index_a += 1
            else:
                index_b += 1
            #           2.3.1 move one of the two indexes
        return []

    def slot_a_is_earlier(self, slot_a, index_a, slot_b, index_b):
        if slot_a[index_a][1] < slot_b[index_b][0]:
            return True
        return False


if __name__ == '__main__':
    case_1_slotA = [[10,50],[60,120],[140,210]]
    case_1_slotB = [[0,15],[60,70]]
    case_1_dur = 24
    case_2_slotA = [[10,50],[60,120]]
    case_2_slotB = [[0,5],[55,60]]
    case_2_dur = 12
    case_3_slotA = [[10,50],[60,120],[140,210]]
    case_3_slotB = [[0,15],[60,70]]
    case_3_dur = 8

    expected_1 = []
    expected_2 = []
    expected_3 = [60,68]

    solution_1 = Solution().solve(case_1_slotA, case_1_slotB, case_1_dur)
    print(solution_1)
    solution_2 = Solution().solve(case_2_slotA, case_2_slotB, case_2_dur)
    solution_3 = Solution().solve(case_3_slotA, case_3_slotB, case_3_dur)

    assert solution_1 == expected_1
    assert solution_2 == expected_2
    assert solution_3 == expected_3