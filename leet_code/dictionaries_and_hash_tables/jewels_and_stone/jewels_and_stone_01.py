# Jewels and Stones
#
# You're given strings J representing the types of stones that are jewels, and S
# representing the stones you have.  Each character in S is a type of stone you
# have. You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are
# letters. Letters are case sensitive, so "a" is considered a different type of
# stone from "A".
#
# Example 1:
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
#
# Input: J = "z", S = "ZZ"
# Output: 0
#

# BRUTE FORCE SOLUTION (has time complexity of O(N*M) and spatial complexity of O(1))

class Solution:
    def numJewelsInStones(self, J, S):
        stone_also_jewel_cnt = 0

        for stone in S:
            if stone in J:
                stone_also_jewel_cnt += 1

        return stone_also_jewel_cnt

# IMPROVED. Improved solution has spatial complexity of O(M) abd spatial complexity of O(N)  where N < M.

    def numJewelsInStonesImproved(self, J, S):
        stone_also_jewel_cnt = 0

        for stone in S:
            if stone in set([x for x in J]):
                stone_also_jewel_cnt += 1

        return stone_also_jewel_cnt


if __name__ == '__main__':
    J = 'aA'
    S = 'aAAbbbb'

    expected = 3

    solution = Solution().numJewelsInStones(J, S)
    solution_improved = Solution().numJewelsInStonesImproved(J, S)

    assert solution == expected
    assert solution_improved == expected
