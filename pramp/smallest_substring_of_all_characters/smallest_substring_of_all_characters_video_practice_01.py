# Smallest Substring of All Characters
#
# Given a string str and array of characters in 'arr', find smallest substring
# in 'str' that has each of character in 'arr'
#
# input:  arr = ['x','y','z'], str = "xyyzyzyx"
#
# output: "zyx"
#
#
# input
#   - array of string 'arr'
#   - string 'str'
#
# output
#   - string
#
# constraint
#   - if no solution exists, then return empty string
#
#
##  arr = ['x','y','z'], str = "xyyzyzyx"

## length == 1
# str = "xyyzyzyx" -> has this all characters in arr ? --> No --> skip
#       | |
#
# str = "xyyzyzyx" -> has this all characters in arr ? --> No --> skip
#        | |
#
# str = "xyyzyzyx" -> has this all characters in arr ? --> No --> skip
#              | |
#
#
# length == 2
# str = "xyyzyzyx" -> has this all characters in arr ? --> No --> skip
#       |  |
#
# ...
#
# str = "xyyzyzyx" -> has this all characters in arr ? --> No --> skip
#             |  |
#
# length == 3
#
# str = "xyyzyzyx" -> has this all characters in arr ? --> No --> skip
#        |  |
#
# ...
# str = "xyyzyzyx" -> has this all characters in arr ? --> YES!! --> return string
#        |      |
#       index  substring_length < len(str)
##
# if solution doesn't exist, reepeat until index + substring_length < len(str)
#
# Pseudocode
class Solution:
    def solve(self, arr, string):
        #   1. initialize substring_length = 0, and index = 0
        substring_length = 0

        while substring_length < len(string):
            index = 0
            while index + substring_length < len(string):
                print(string[index: index + substring_length + 1])
                #   2. check if substring from index to index + substring_length has all the characters in arr
                if self.hasAllCharactersInArr(arr, string, index, substring_length):
                    #   3. if it has all the characters, return the substring str[index: index + substring_length + 1]
                    return string[index: index + substring_length + 1]

                index += 1

            #   4. increment index until index + substring_length < len(str)
            substring_length += 1

        return ""

    def hasAllCharactersInArr(self, arr, string, index_start, substring_length):
        index = index_start
        index_end = index_start + substring_length + 1
        char_dict = {}

        while index < index_end:
            char = string[index]
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
            index += 1

        for char in arr:
            if char not in char_dict:
                return False

        return True

# Time complexity --> O(N^3), Spatial complexity --> O(1)


if __name__ == '__main__':
    case_1_arr = ['x','y','z']
    case_1_str = "xyyzyzyx"


    case_2_arr = ['x','w','z']
    case_2_str = "xyyzyzyx"

    expected_1 = "xyz"
    expected_2 = ""

    solution_1 = Solution().solve(case_1_arr, expected_1)
    print(solution_1)
    solution_2 = Solution().solve(case_2_arr, expected_2)

    assert expected_1 == solution_1
    assert expected_2 == solution_2