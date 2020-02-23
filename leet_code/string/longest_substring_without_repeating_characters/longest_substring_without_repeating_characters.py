#  Longest Substring Without Repeating Characters
#
# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # move front as long as front is less than n and letter not in set
        # also, increment substring count

        if len(s) == 0:
            return 0

        letters_set = set()
        N = len(s)
        front, length, max_length = 0, 1, 1
        for back in range(N):
            while (front < N) and (s[front] not in letters_set):
                letters_set.add(s[front])
                front += 1

            length = (front - back)
            max_length = max(length, max_length)
            letters_set.remove(s[back])

        return max_length


