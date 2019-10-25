# Sentence Reverse
#
# You are given an array of characters arr that consists of sequences of characters
# separated by space characters. Each space-delimited sequence of characters defines
# a word.
#
# Implement a function reverseWords that reverses the order of the words in the
# array in the most efficient manner.
#
# Explain your solution and analyze its time and space complexities.
#
# Example:
#
# input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
#                 'm', 'a', 'k', 'e', 's', '  ',
#                 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
#
# output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
#           'm', 'a', 'k', 'e', 's', '  ',
#           'p', 'e', 'r', 'f', 'e', 'c', 't' ]
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.character arr
#
# 0 ≤ arr.length ≤ 100
# [output] array.character
#
# Brute force solution
# Pseudocode (Brute force solution):

#   1. combine characters into a sentence
#   2. split sentence by space
#   3. flip the words around
#   4. parse the words
#   5. return the output
#
# note that this has time complexity of O(N) and spatial complexity of O(N)

# Improved solution

#   1. initialize index_word_start = None and index_word_end = None
#   2. flip all characters in arr
#   3. for each character in arr,
#       3.1 if the character is the beginning of the first word, set index_word_start = index of the character
#       3.2 if the character is the end of the first word, set index_word_end = index of character, and flip characters from index_word_start to index_word_end
#       3.3 once all done, reset index_word_start and index_word_end to None
#
#   4. return output
#
# TIme complexity O(N), and spatial complexity O(1)

import re

class Solution:
    def solve(self, arr):
        #   1. initialize index_word_start = None and index_word_end = None
        index_word_start = None
        index = 0
        print('-------')
        #   2. flip all characters in arr
        arr = arr[::-1]

        while index < len(arr):
            #   3. for each character in arr,
            #       3.1 if the character is the beginning of the first word, set index_word_start = index of the character
            if self.start_of_word(index, arr, index_word_start):
                index_word_start = index

            #       3.2 if the character is the end of the first word, set index_word_end = index of character, and flip characters from index_word_start to index_word_end
            elif self.end_of_word(index, arr, index_word_start):
                if index_word_start == None:
                    index += 1
                    continue

                index_word_end = None

                if arr[index] == ' ':
                    index_word_end = index - 1
                else:
                    index_word_end = index

                self.flip(arr, index_word_start, index_word_end)

                index_word_start = None

            #       3.3 once all done, reset index_word_start and index_word_end to None
            index +=1

        return arr

    def start_of_word(self, index, arr, index_word_start):
        # 1.is not a start of a word
        if arr[index] != ' ' and index_word_start == None:
            return True

        # 3. otherwise return False
        return False

    def end_of_word(self, index, arr, index_word_start):
        if arr[index] == ' ' and index_word_start != None:
            return True

        if index == len(arr) - 1 and index_word_start != None:
            return True

        return False

    def flip(self, arr, index_word_start, index_word_end):

        while index_word_start < index_word_end:
            arr[index_word_start], arr[index_word_end] = arr[index_word_end], arr[index_word_start]

            index_word_start += 1
            index_word_end -= 1




# TIme complexity O(N), and spatial complexity O(1)


if __name__ == '__main__':
    case_1 = [" "," "]
    case_2 = ["a"," "," ","b"]
    case_3 = ["h","e","l","l","o"]
    case_4 = ["p","e","r","f","e","c","t"," ","m","a","k","e","s"," ","p","r","a","c","t","i","c","e"]
    case_5 = ["y","o","u"," ","w","i","t","h"," ","b","e"," ","f","o","r","c","e"," ","t","h","e"," ","m","a","y"]
    case_6 = ["g","r","e","a","t","e","s","t"," ","n","a","m","e"," ","f","i","r","s","t"," ","e","v","e","r"," ","n","a","m","e"," ","l","a","s","t"]

    expected_1 =  [" "," "]
    expected_2 =  ["b"," "," ","a"]
    expected_3 = ["h","e","l","l","o"]
    expected_4 = ["p","r","a","c","t","i","c","e"," ","m","a","k","e","s"," ","p","e","r","f","e","c","t"]
    expected_5 =  ["m","a","y"," ","t","h","e"," ","f","o","r","c","e"," ","b","e"," ","w","i","t","h"," ","y","o","u"]
    expected_6 = ["l","a","s","t"," ","n","a","m","e"," ","e","v","e","r"," ","f","i","r","s","t"," ","n","a","m","e"," ","g","r","e","a","t","e","s","t"]

    solution_1 = Solution().solve(case_1)
    solution_2 = Solution().solve(case_2)
    solution_3 = Solution().solve(case_3)
    print(solution_3)
    solution_4 = Solution().solve(case_4)
    solution_5 = Solution().solve(case_5)
    solution_6 = Solution().solve(case_6)


    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4
    assert expected_5 == solution_5
    assert expected_6 == solution_6





