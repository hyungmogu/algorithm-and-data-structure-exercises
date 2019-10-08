# Permutation Palindrome
#
# Write an efficient function that checks whether any permutation
# of an input string is a palindrome.
#
# Example
#   "civic" should return True
#   "ivicc" should return True
#   "civil" should return False
#   "livci" should return False

# Known
#   - Key characteristic of Palindrome
#       - Palindrome can have at most 1 odd number of characters. Everything else must be even!
#

# This solution has spatial complexity of O(N) and time complexity O(N)

class Solution:
    def permutationPalindrome(self, letters):
        # Pseudocode
        # 1. count characters and store in dictionary
            character_cnt = {}
            key_with_odd_cnt = 0

            for letter in letters:
                if letter in character_cnt:
                    character_cnt[letter] += 1
                else:
                    character_cnt[letter] = 1

        # 2. for each key in dictionary,
        # 2.1 if there are more than 1 number of keys with odd number of characters, return False
        # 2.2 else return true
            for key in character_cnt:
                if character_cnt[key] % 2 != 0:
                    key_with_odd_cnt += 1

            if key_with_odd_cnt > 1:
                return False

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