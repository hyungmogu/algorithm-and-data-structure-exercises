# Sentence Reverse
#
# given an array of characters (sentence separated by spaces), create an algorithm
# that reverses the order of words
#
#
# constraint
#   - there are NO spaces after the end of a word or in front of a word for an input
#       [" ","p","e","r","f","e","c","t"," ","m","a","k","e","s"," ","p","r","a","c","t","i","c","e"] --> NO.
#       ["p","e","r","f","e","c","t"," ","m","a","k","e","s"," ","p","r","a","c","t","i","c","e", " "] --> NO
#   - length of array is in between 0 and 100
#   - element in arr is either an alphabet or space
#
# input
#   - an array of characters
#
# output
#   - an array of characters
#
# Example (brute force)
#
# ["p","e","r","f","e","c","t"," ","m","a","k","e","s"," ","p","r","a","c","t","i","c","e"] -->
#   --> "perfect makes practice" --> ['perfect', 'makes', 'practice'] --> 'perfect makes practice'
#
# pseudocode (brute force)
#   1. join arr into a string --> + O(N)
#   2. split the string by space --> O(M) where M < N
#   3. reverse the words --> O(1)
#   4. join the words together by space --> O(N)
#   5. split all characters and return array --> O(N)
#
#   time complexity O(N) and spatial complexity is O(N)
#
#
#  time complexity O(N) and spatial complexity of O(1)
#
# ['h','i',' ','y','o'] --> ['o','y',' ','i','h'] (in-place)
#
#  ['o','y',' ','i','h'] --> ['y','o',' ','h','i']
#    x
#
# ["p","e","r","f","e","c","t"," ","m","a","k","e","s"," ","p","r","a","c","t","i","c","e"]
#
#   --> [e,c,i,t,c,a,r,p, ,s,e,k,a,m, ,t,c,e,f,r,e,p]
#   --> [p,r,a,c,t,i,c,e, ,m,a,k,e,s, ,p,e,r,f,e,c,t]
# cases
#   1. len(arr) == 0
#   2. len(arr) == 1
#   3. len(arr) !== 1
#
# pseudocode
#   1. if arr is empty, return empty array
#   2. if arr has length 1, return array
#
#   3. reverse all characters in words
#   4. starting from the beginning of array
#       4.1 if is the beginning of word, set index_word_start = index
#       4.2 if is the end of word, and is space, flip from index_word_start to index_word_end -1
#       4.3 if is the ned of word, and is the end of array, flip from flip index_word_start to index_word_end
#
# Time Complexity O(N), and spatial complexity O(1)


class Solution:
    def solve(self, arr):
        #   1. if arr is empty, return empty array
        #   2. if arr has length 1, return array
        if len(arr) == 0 or len(arr) == 1:
            return arr

        #   3. reverse all characters in words
        self.flip(arr, 0, len(arr) - 1)

        index = 0
        index_word_start = None
        index_word_end = None

        #   4. starting from the beginning of array
        while index < len(arr):
            #       4.1 if is the beginning of word, set index_word_start = index
            if self.start_of_word(arr, index, index_word_start):
                index_word_start = index
                print(index_word_start)

            #       4.2 if is the end of word, and is space, flip from index_word_start to index_word_end -1
            #       4.3 if is the ned of word, and is the end of array, flip from flip index_word_start to index_word_end
            elif self.end_of_word(arr, index, index_word_start):
                if arr[index] == ' ':
                    index_word_end = index - 1
                else:
                    index_word_end = index

                self.flip(arr, index_word_start, index_word_end)
                print(arr)

                index_word_start = None
                index_word_end = None


            index += 1
            # Time Complexity O(N), and spatial complexity O(1)

        return arr

    def start_of_word(self, arr, index, index_word_start):
        if arr[index] != ' ' and index_word_start == None:
            return True
        return False

    def end_of_word(self, arr, index, index_word_start):
        if index == len(arr) - 1 and index_word_start != None:
            return True

        if arr[index] == ' ' and index_word_start != None:
            return True

        return False

    def flip(self, arr, index_word_start, index_word_end):
        # [a,b,c] -> [c,b,a], --> flip first with last, second with second last
        # [a,b,c,d] --> [d,c,b,a]

        while index_word_start < index_word_end:
            arr[index_word_start], arr[index_word_end] = arr[index_word_end], arr[index_word_start]

            index_word_start += 1
            index_word_end -= 1


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

