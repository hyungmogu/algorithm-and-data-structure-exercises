# Deletion Distance
# The deletion distance of two strings is the minimum number of characters you
# need to delete in the two strings in order to get the same string. For instance,
# the deletion distance between "heat" and "hit" is 3:

# By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in
# both cases.
# We cannot get the same string from both strings by deleting 2 letters or fewer.
# Given the strings str1 and str2, write an efficient function deletionDistance
# that returns the deletion distance between them. Explain how your function works,
# and analyze its time and space complexities.

# Examples:

# input:  str1 = "dog", str2 = "frog"
# output: 3

# input:  str1 = "some", str2 = "some"
# output: 0

# input:  str1 = "some", str2 = "thing"
# output: 9

# input:  str1 = "", str2 = ""
# output: 0


#       ''  d   o   g
#
#   ''  0   1   2   3
#   f   1   2   3   4
#   r   2   3   4   5
#   o   3   4   3   4
#   g   4   5   4   3
#
#   row -> index_i
#   col -> index_j
#
#       ''  d   o   g (str_2)
#
#  [ ''  0   1   2   3 ] prev ->
#  [ f   1   2   3   4 ] curr ->
#  [ r   2   3   4   5 ]
#  [ o   3   4   3   4 ]
#  [ g   4   5   4   3 ]
#    ^
#    str_1
#
# pseudocode
#   1. initialize curr and prev list
#       i.e. curr = [0, 0, 0, 0] prev = [0, 0, 0, 0]
#
#   1. if index_i == 0, then set curr[index_j] = index_j
#       i.e. (index_i == 0) curr = [0, 1, 2, 3, 4]
#
#   2. if index_i !== 0, and
#   2.1 if index_j == 0, then set curr[index_j] = index_i
#   2.2 if index_j != 0, and str_1[index_i] == str_2[index_j], curr[index_j] = prev[index_j-1]
#   2.3 if index_j != 0, and str_1[index_j] != str_2[index_j], curr[index_j] = 1 + min(curr[index_j-1], prev[index_j])
#   3. swap curr with prev
#   4. reinitialize curr
#
#   5. once all done, return curr[-1]

class Solution:
    def deletion_distance(self, str_1, str_2):
        index_i = 0
        str_1 = ' ' + str_1
        str_2 = ' ' + str_2

        if len(str_1) < len(str_2):
            str_1, str_2 = str_2, str_1

        #   1. initialize curr and prev list
        #       i.e. curr = [0, 0, 0, 0] prev = [0, 0, 0, 0]
        curr = [0] * len(str_2)
        prev = [0] * len(str_2)

        while index_i < len(str_1):
            index_j = 0
            while index_j < len(str_2):
                # print(index_j)
                #   1. if index_i == 0, then set curr[index_j] = index_j
                if index_i == 0:
                    curr[index_j] = index_j
                    index_j += 1
                    continue
                #   2. if index_i !== 0, and
                #   2.1 if index_j == 0, then set curr[index_j] = index_i
                if index_j == 0:
                    curr[index_j] = index_i
                    index_j += 1
                    continue
                #   2.2 if index_j != 0, and str_1[index_i] == str_2[index_j], curr[index_j] = prev[index_j-1]

                if index_j != 0 and str_1[index_i] == str_2[index_j]:
                    curr[index_j] = prev[index_j-1]
                    index_j += 1
                    continue
                #   2.3 if index_j != 0, and str_1[index_j] != str_2[index_j], curr[index_j] = 1 + min(curr[index_j-1], prev[index_j])
                if index_j != 0 and str_1[index_i] != str_2[index_j]:
                    curr[index_j] = 1 + min(curr[index_j-1], prev[index_j])
                    index_j += 1
                    continue

            #   3. swap curr with prev
            #   4. reinitialize curr
            curr, prev = prev, curr
            curr = [0] * len(str_2)
            index_i += 1

        #   5. once all done, return curr[-1]
        return prev[-1]


if __name__ == '__main__':
    str_1_case_1 = ""
    str_2_case_1 = "hit"

    str_1_case_2 = "neat"
    str_2_case_2 = ""

    str_1_case_3 = "heat"
    str_2_case_3 = "hit"

    str_1_case_4 = "hot"
    str_2_case_4 = "not"

    str_1_case_5 = "some"
    str_2_case_5 = "thing"

    str_1_case_6 = "abc"
    str_2_case_6 = "adbc"

    str_1_case_7 = "awesome"
    str_2_case_7 = "awesome"

    expected_1 = 3
    expected_2 = 4
    expected_3 = 3
    expected_4 = 2
    expected_5 = 9
    expected_6 = 1
    expected_7 = 0

    solution_1 = Solution().deletion_distance(str_1_case_1, str_2_case_1)
    solution_2 = Solution().deletion_distance(str_1_case_2, str_2_case_2)
    solution_3 = Solution().deletion_distance(str_1_case_3, str_2_case_3)
    solution_4 = Solution().deletion_distance(str_1_case_4, str_2_case_4)
    solution_5 = Solution().deletion_distance(str_1_case_5, str_2_case_5)
    solution_6 = Solution().deletion_distance(str_1_case_6, str_2_case_6)
    solution_7 = Solution().deletion_distance(str_1_case_7, str_2_case_7)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4
    assert expected_5 == solution_5
    assert expected_6 == solution_6
    assert expected_7 == solution_7