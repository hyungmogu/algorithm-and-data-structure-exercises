# Permutation of Characters
#
# Write a recursive function for generating all permutations of an input string.
# Return them as a set.
#
# cat -> {cat, cta, tac, tca, atc, act}
#
#
#
#
# Input
#   - String
#
# Output
#   - Set of Characters
#
# known
#   - the problem needs to be solved using dynamic programming
#
#
# Brute force approach
#   1. split the word into array of cahracters
#   2. for each character, try all combinations of letters
#   3. for each combination, check and see if it has right number of characters
#   4. if so, pass to set. otherwise, reject it
#
#
#   Time complexity O(N^N) and spatial complexity O(N)
#
#
#
# Dynamic Programming --> Better
#   1. characterized by dividing a problem into subproblems using recursion
#       - take away something until it reaches the base condition (that something cannot be removed any further)
#       - once base condition is achieved, perform an operation that will find all permutation of letters in a word

#   2. characterized by usage of memoization (speeds up process of dynamic programming by storing redundant calculations in dictionary)


class Solution:
    def permutationOfCharacters(self, characters):
        # 0. if base condition (length of word == 1) return { word }
        if len(characters) == 1:
            return {characters}

        # 1. divide the problem into subproblems by taking away the last character of a word
        # {'c'}
        # last_character = 'a'
        # cat
        last_character = characters[-1]

        characters_without_last_set = self.permutationOfCharacters(characters[:-1])
        # {'c'}

        # 2. find all possible combinations of characters
        # ca, ac
        # [:position] + last_character + [position:]
        result = set()
        for combination_characters in characters_without_last_set:
            for position_index in range(len(combination_characters)+1):
                combination = (
                    combination_characters[:position_index] +
                    last_character +
                    combination_characters[position_index:]
                )

                result.add(combination)


        # Place the combination to a set
        return result


if __name__ == '__main__':
    case_1 = 'cat'
    case_2 = 'ca'
    case_3 = 'c'

    expected_1 = {'cat', 'cta', 'tac', 'tca', 'atc', 'act'}
    expected_2 = {'ac', 'ca'}
    expected_3 = {'c'}

    solution_1 = Solution().permutationOfCharacters(case_1)
    print(solution_1)
    solution_2 = Solution().permutationOfCharacters(case_2)
    solution_3 = Solution().permutationOfCharacters(case_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
