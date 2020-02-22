# Permutation of Characters
#
# Write a recursive function for generating all permutations of an input string.
# Return them as a set.
#
# cat -> {cat, cta, tac, tca, atc, act}
#
# CONDITION: Solve using Dynamic Programming

class Solution:
    def permutationOfCharacters(self, characters):

        if len(characters) == 1:
            return set(characters)

        last_character = characters[-1]
        characters_except_last = characters[:-1] # get all characters but last

        permutation_characters_except_last_set = self.permutationOfCharacters(characters_except_last)

        new_permutation_characters_set = set()
        for permutation_characters in permutation_characters_except_last_set:
            for character_position in range(len(permutation_characters) + 1):
                new_permutation = (
                    permutation_characters[:character_position] +
                    last_character +
                    permutation_characters[character_position:]
                )

                new_permutation_characters_set.add(new_permutation)

        return new_permutation_characters_set


if __name__ == '__main__':
    case_1 = 'cat'
    case_2 = 'ca'
    case_3 = 'c'

    expected_1 = {'cat', 'cta', 'tac', 'tca', 'atc', 'act'}
    expected_2 = {'ac', 'ca'}
    expected_3 = {'c'}

    solution_1 = Solution().permutationOfCharacters(case_1)
    solution_2 = Solution().permutationOfCharacters(case_2)
    solution_3 = Solution().permutationOfCharacters(case_3)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3

