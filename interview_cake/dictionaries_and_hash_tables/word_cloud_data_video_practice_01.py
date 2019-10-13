# Word Cloud Data
#
# You want to build a word cloud, an infographic where the size of a word
# corresponds to how often it appears in the body of text.
#
# To do this, you'll need data. Write code that takes a long string and builds
# its word cloud data in a dictionary, where the keys are words and the values
# are the number of times the words occurred.
#
# Think about capitalized words. For example, look at these sentences:
#
#   'After beating the eggs, Dana read the next step:' -->  {'after': 1, 'beating': 1, 'the': 2, 'eggs': 1, 'dana': 1, 'read': 1, 'step': 1, 'next': 1}
#   'Add milk and eggs, then add flour and sugar.' --> {'add': 2, 'milk': 1, 'and': 2 , 'eggs': 1, 'then': 1, 'flour': 1, 'sugar': 1}
#
# What do we want to do with "After", "Dana", and "add"? In this example, your
# final dictionary should include one "Add" or "add" with a value of 22. Make
# reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".
#
# Assume the input will only contain words and standard punctuation.
#
#
# input
#   - string
# output
#   - dictionary
#
# 'After beating the eggs, Dana read the next step:'
# 'after beating the eggs, dana read the next step:'
# 'after beating the eggs dana read the next step'
# [after, beatings, the, eggs]
# {'after': 1, 'beating': 1, 'the': 2, 'eggs': 1, 'dana': 1, 'read': 1, 'step': 1, 'next': 1}
#
#
# Pseudocode
#     word_frequency = {}

# #   1. turn all string into lowercase letters
#     words = words.lower()

# #   2. remove all symbols except spaces
#     words = re.sub(r'[^a-z\s]', '', words)

# #   3. count words
#     for word in words:
#         if word in word_frequency:
#             word_frequency[word] += 1
#         else:
#             word_frequency[word] = 1

# #   4. return word_frequency
#     return word_frequency

# O(N) where N represents number of characters in string, spatial - O(N)


import re

class Solution:
    def wordCloudData(self, words):
        word_frequency = {}

        #   1. turn all string into lowercase letters
        words = words.lower()

        #   2. remove all symbols except spaces
        words = re.sub(r'[^a-z\s]', '', words)

        #   3. count words
        for word in words.split():
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        #   4. return word_frequency
        return word_frequency


if __name__ == '__main__':
    case_1 = 'After beating the eggs, Dana read the next step:'
    case_2 = 'Add milk and eggs, then add flour and sugar.'
    case_3 = ''

    expected_1 = {'after': 1, 'beating': 1, 'the': 2, 'eggs': 1, 'dana': 1, 'read': 1, 'step': 1, 'next': 1}
    expected_2 = {'add': 2, 'milk': 1, 'and': 2 , 'eggs': 1, 'then': 1, 'flour': 1, 'sugar': 1}
    expected_3 = {}

    solution_1 = Solution().wordCloudData(case_1)

    solution_2 = Solution().wordCloudData(case_2)
    solution_3 = Solution().wordCloudData(case_3)

    for key in solution_1.keys():
        assert expected_1[key] == solution_1[key]

    for key in solution_2.keys():
        assert expected_2[key] == solution_2[key]

    assert expected_3 == solution_3