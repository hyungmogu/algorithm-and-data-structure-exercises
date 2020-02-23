# Valid Anagram
#
# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# =========== solution ===============

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_letter_cnt = {}

        for letter in s:
            if letter not in s_letter_cnt:
                s_letter_cnt[letter] = 1
            else:
                s_letter_cnt[letter] += 1

        for letter in t:
            if letter not in s_letter_cnt:
                return False

            if s_letter_cnt[letter] == 0:
                return False

            s_letter_cnt[letter] -= 1

        keys = s_letter_cnt.keys()

        for key in keys:
            if s_letter_cnt[key] > 0:
                return False

        return True

