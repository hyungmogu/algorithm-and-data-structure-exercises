# Permutation Palindrome
#
# Write an efficient function that checks whether any permutation
# of an input string is a palindrome.
#
# Example
#   "civic" should return True
#   "ivicc" should return True
#   "civil" should return False
#   "icvli" --> "ilvci"
#   "livci" should return False
#
# Input
#   letters (string)
#
# Output
#   boolean (True if palindrome, and False if not palindrome)
#
# Known
#   - Key characteristic of Palindrome
#       - Palindrome can have at most 1 odd number of characters. Everything else must be even!
#

# This solution has spatial complexity of O(M) and time complexity O(M)

class Solution:
    def permutationPalindrome(self, letters):
        # Brute force solution
        #   1. count characters in 'letters', and store inside dictionary 'character_count'
        #   {'c': 2, 'i': 2, 'v': 1}
        character_count = {}

        for character in letters:
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1

        #   2. count characters with odd number of count for each key in character_count, 'char_with_odd_count'
        #   char_with_odd_count = 1
        char_with_odd_count = 0

        for character in character_count:
            if character_count[character] % 2 != 0:
                char_with_odd_count += 1

        #   3. if char_with_odd_count > 1, return False
        if char_with_odd_count > 1:
            return False

        #   4. return True
        return True

if __name__ == "__main__":
    case_1 = "civic"
    case_2 = "ivicc"
    case_3 = "civil"
    case_4 = "livci"

    expected_1 = True
    expected_2 = True
    expected_3 = False
    expected_4 = False

    solution_1 = Solution().permutationPalindrome(case_1)
    solution_2 = Solution().permutationPalindrome(case_2)
    solution_3 = Solution().permutationPalindrome(case_3)
    solution_4 = Solution().permutationPalindrome(case_4)

    assert expected_1 == solution_1
    assert expected_2 == solution_2
    assert expected_3 == solution_3
    assert expected_4 == solution_4