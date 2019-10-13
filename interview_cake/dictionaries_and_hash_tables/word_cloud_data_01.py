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
#   'After beating the eggs, Dana read the next step:'
#   'Add milk and eggs, then add flour and sugar.'
#
# What do we want to do with "After", "Dana", and "add"? In this example, your
# final dictionary should include one "Add" or "add" with a value of 22. Make
# reasonable (not necessarily perfect) decisions about cases like "After" and "Dana".
#
# Assume the input will only contain words and standard punctuation.
#

# import re

# word_frequency = {}

# # Solution - O(N) time complexity where N represents the length of words
# # 1. turn all words into lowercase
# words = words.lower()
# # 2. remove all special characters
# words = re.sub(r'[^a-z\s]' , '', words)

# # 3. split words by space
# words = words.split()

# # 4. for each word, count its frequency and store in 'word_frequency'
# for word in words:
#     if word in word_frequency:
#         word_frequency[word] += 1
#     else:
#         word_frequency[word] = 1

# # 5. return word_frequency
# return word_frequency


import re

class Solution:
    def wordCloudData(self, words):
        word_frequency = {}

        # Solution - O(N) time complexity where N represents the length of words
        # 1. turn all words into lowercase
        words = words.lower()
        # 2. remove all special characters
        words = re.sub(r'[^a-z\s]' , '', words)

        # 3. split words by space
        words = words.split()

        # 4. for each word, count its frequency and store in 'word_frequency'
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        # 5. return word_frequency
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