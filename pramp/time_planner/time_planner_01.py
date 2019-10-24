# Time Planner
# Implement a function meetingPlanner that given the availability, slotsA and
#slotsB, of two people and a meeting duration dur, returns the earliest time slot
#that works for both of them and is of duration dur. If there is no common time
#slot that satisfies the duration requirement, return an empty array.
#
# Time is given in a Unix format called Epoch, which is a nonnegative integer
#holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.
#
# Each person's availability is represented by an array of pairs. Each pair is
#an epoch array of size two. The first epoch in a pair represents the start time
#of a slot. The second epoch is the end time of that slot. The input variable dur
#is a positive integer that represents the duration of a meeting in seconds. The
#output is also a pair represented by an epoch array of size two.
#
# In your implementation assume that the time slots in a person's availability
#are disjointed, i.e, time slots in a person's availability don't overlap. Further
#assume that the slots are sorted by slots' start time.
#
# Implement an efficient solution and analyze its time and space complexities.
#
# Examples:
#
# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 8
# output: [60, 68]
#
# input:  slotsA = [[10, 50], [60, 120], [140, 210]]
#         slotsB = [[0, 15], [60, 70]]
#         dur = 12
# output: [] # since there is no common slot whose duration is 12
# Constraints:
#
# [time limit] 5000ms
#
# cases
# 1. when two don't overlap
#  [10, 50] --> using [max(slot_a[index_a][0], slot_b[index_b][0]), min(slot_a[index_a][1],slob_b[index_b][1])]
#  [60, 80]     --> [60, 50]
#

# 2. when two overlap and they overlap partially
#  [10, 50] --> [15, 50] --> [max(slot_a[index_a][0], slot_b[index_b][0]), min(slot_a[index_a][1],slob_b[index_b][1])]
#  [15, 70]

# 3. when two overlap and one is in the other
#  [10, 50] --> [15, 20] --> [max(slot_a[index_a][0], slot_b[index_b][0]), min(slot_a[index_a][1],slob_b[index_b][1])]
#  [15, 20]

# time complexity O(N + M), spatial complexity --> O(1)

# pseudocode
class Solution:
    def solve(self, slot_a, slot_b, duration):
        index_b = 0
        index_a = 0

        #   1. if len(slotB) > len(slotA), swap the two
        if len(slot_b) > len(slot_a):
            slot_b, slot_a = slot_a, slot_b

        #   2. for each pointer index_slotB in slotB, find duration with the element under
        #   the pointer index_slotA in slotA,
        while index_a < len(slot_a) and index_b < len(slot_b):
            #       2.1 find start_time and end_time
            start_time = max(slot_a[index_a][0], slot_b[index_b][0])
            end_time = min(slot_a[index_a][1],slot_b[index_b][1])

            #       2.2 find overlap and store in 'current_duration'
            overlap = end_time - start_time

            #       2.3 if current_duration exists and current_duration > duration return [start_time, start_time + duration]
            if overlap > 0 and overlap > duration:
                return [start_time, start_time + duration]

            #       2.1 find duration with the element under the pointer index_slotA
            if self.slot_a_is_earlier(slot_a, index_a, slot_b, index_b):
                index_a += 1
            else:
                index_b += 1

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