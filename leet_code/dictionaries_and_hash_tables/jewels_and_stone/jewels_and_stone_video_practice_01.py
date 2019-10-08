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

# Input (String J, String S)
# Output Int

# Known
#    - len(S) > len(J)

# Brute force solution
# stone_also_jewel_cnt = 0

# 1. for each stone in S
    # for stone in S:

# 1.1 if stone in J, raise stone_also_jewel_cnt by 1
        # if stone in J:
        #     stone_also_jewel_cnt += 1

# 2. return stone_also_jewel_cnt

    # return stone_also_jewel_cnt


# time complexity O(N * M) where N is len(J) and M is len(S)
# spatial complexity O(1)

# sets() --> {a, b, c, d} O(1)

# O(N * M) --> O(1 * M) --> O(M)


class Solution:
    def numJewelsInStones(self, J, S):
        stone_also_jewel_cnt = 0

        # 1. for each stone in S
        for stone in S:

        # 1.1 if stone in J, raise stone_also_jewel_cnt by 1
            if stone in set([x for x in J]):
                stone_also_jewel_cnt += 1

        # 2. return stone_also_jewel_cnt

        return stone_also_jewel_cnt


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"

    expected = 3

    solution = Solution().numJewelsInStones(J,S)

    assert solution == expected
