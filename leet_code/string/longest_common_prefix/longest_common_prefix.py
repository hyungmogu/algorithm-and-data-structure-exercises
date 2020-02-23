#  Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


#============= solution ==============

import sys

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_index = 0
        word_count = sys.maxsize
        min_word = ''

        common_prefix = ''

        for (index, word) in enumerate(strs):
            if len(word) < word_count:
                min_word = word
                word_count = len(word)
                min_index = index

        if not min_word:
            return ""

        for (index, letter) in enumerate(min_word):

            for word in strs:
                if word[index] != letter:
                    return common_prefix

            common_prefix += letter

        return common_prefix




