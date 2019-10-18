# Given the input array of characters, and string
# find the smallest string that has all characters
# in arr

# arr = ['x','y','z'], str = "xyyzyzyx"
#
# "zyx"
#
#
# constraint
#   - the substring must be of minimum length
#   - can be of any combination
#
# known
#   - base condition occurs when the two pointers cross, also when one character has count of 0
#     - determine the length of string compare with the current minimum, and replace if smaller
#
#   - recursion is used --> because it's exploring all possible combinations between index_left and index_right
#     - modification of fibonacci sum will be used
#
#
#       fib(left_index + 1) + fib(right_index - 1)
#
#
# {x: 2, y: 4, z: 2}
#
# length 4
#
#
# length = 0
# now i am at length of 3
# "xyyzyzyx"    --> calculate length of solution --> 8
#  ^
#     * index + length
#
# length = 1
# "xyyzyzyx"    --> calculate length of solution --> 8
#  ^
#   * index + length

#length = 2
# "xyyzyzyx"    --> calculate length of solution --> 8
#       ^
#          * index + length
# str[index:index+length] -> str[index:index] ->
#
#  index, index+length
# O(N), spatial complexity O(1)

# 1. for length between [0 ... len(string)]
# 2. if characters in between the length satisfies the minimum required, return result
# 3. if minimum not satisfied,
#
#
#


def get_shortest_unique_substring(arr, str):

  if len(str) == 1 and condition_satisfied(arr, str, 0, 1):
    return str

  for length in range (len(arr), len(str)):
    index = 0

    while index + length < len(str):
      if condition_satisfied(arr, str, index, length):
        return str[index:index+length]

      index+=1

  return ""


def condition_satisfied(arr, str, index, length):
  char_count = {}
  substring = str[index: index+length]

  # initialize count

  for char in substring:
    char_count[char] += 1


  for char in arr:
    if char not in char_count:
      return False

  return True


'''
if __name__ == '__main__':
  arr = ['x','y','z']
  str = "xyyzyzyx"

  expected = 'zyx'
  solution = get_shortest_unique_substring(arr, str)

  assert expected == solution
 '''

