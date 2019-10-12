# Word Count Engine
# Implement a document scanning function wordCountEngine, which receives a
# string document and returns a list of all unique words in it and their number
# of occurrences, sorted by the number of occurrences in a descending order.
# If two or more words have the same count, they should be sorted according to
# their order in the original sentence. Assume that all letters are in english
# alphabet. You function should be case-insensitive, so for instance, the words
# “Perfect” and “perfect” should be considered the same word.
#
# The engine should strip out punctuation (even in the middle of a word) and use
# whitespaces to separate words.
#
# Analyze the time and space complexities of your solution. Try to optimize for
# time while keeping a polynomial space complexity.
#
# Examples:
#
# input:  document = "Practice makes perfect. you'll only
#                     get Perfect by practice. just practice!"
#
# output: [ ["practice", "3"], ["perfect", "2"],
#           ["makes", "1"], ["youll", "1"], ["only", "1"],
#           ["get", "1"], ["by", "1"], ["just", "1"] ]
#
# Important: please convert the occurrence integers in the output list to
# strings (e.g. "3" instead of 3). We ask this because in compiled languages
# such as C#, Java, C++, C etc., it’s not straightforward to create mixed-type
# arrays (as it is, for instance, in scripted languages like JavaScript, Python,
# Ruby etc.). The expected output will simply be an array of string arrays.
#
# Constraints:
#
# [time limit] 5000ms
# [input] string document
# [output] array.array.string


import re
from collections import OrderedDict

def word_count_engine(document):
    document = document.lower()
    document = re.sub(r'[^a-z\s]', '', document)

    document_list = document.split()

    temp_dict = OrderedDict()

    for word in document_list:
        if word in temp_dict:
            temp_dict[word] += 1
        else:
            temp_dict[word] = 1


    max_count = 0
    for word in temp_dict:
        if temp_dict[word] > max_count:
            max_count = temp_dict[word]

    temp_dict2 = OrderedDict()
    for key in temp_dict:
        frequency = str(temp_dict[key])

        if frequency in temp_dict2:
            temp_dict2[frequency].append(key)
        else:
            temp_dict2[frequency] = [key]

    output = []
    for possible_frequency in reversed(range(0, max_count+1)):
        if str(possible_frequency) in temp_dict2:
            for word in tem_dict2[possible_frequency]:
                output.append([word, str(possible_frequency)])

    return output

