 # Array Index & Element Equality
#
# Given a sorted array arr of distinct integers, write a function
# indexEqualsValueSearch that returns the lowest index i for which arr[i] == i.
# Return -1 if there is no such index. Analyze the time and space complexities of
# your solution and explain its correctness.
#
# Examples:
#
# input: arr = [-8,0,2,5]
# output: 2 # since arr[2] == 2
#
# input: arr = [-1,0,3,6]
# output: -1 # since no index in arr satisfies arr[i] == i.
# Constraints:
#
# [time limit] 5000ms
#
# [input] array.integer arr
#
# 1 <= arr.length <= 100
# [output] integer
# =====================================================================

# given arr of integers, find index such that arr[index] == index
#
# input
#   - list of integers
# ouput
#   - integer
#
#
# restriction
#   - return the lowest index
#
#
# [-8,0,2,5]
#       x
#
# [-1,0,3,6]
# .         x
#
#
# [-8,0,2,5]
#   0 1 2 3
#
# [-8,-1,0,2]
#      1 2   4
#        x
#  arr[index] === index
# arr[index] - index === 0
#
# pseudocode

#floor_index = -1
#ceiling_index = len(arr)

# 1. find the minddle index 'middle_index'
# 2. check if arr[middle_index] == middle_index
# 3. if arr[middle_index] == middle_index, return arr[middle_index]
# 4. if not equal, calculate arr[middle_index] - middle_index
# 4.1 if calculate arr[middle_index] - middle_index > 0, set ceiling_index == middle_index
# 4.2 if calculate arr[middle_index] - middle_index < 0, set floor_index == middle_index

# O(lgN) , spatial O(1)
def index_equals_value_search(arr):
  floor_index = -1
  ceiling_index = len(arr)

  while (floor_index + 1) < ceiling_index:
    # 1. find the minddle index 'middle_index'
    half_distance = (ceiling_index - floor_index) / 2
    middle_index = floor_index + half_distance

    # 2. check if arr[middle_index] == middle_index
    # 3. if arr[middle_index] == middle_index, return arr[middle_index]
    if arr[middle_index] == middle_index:
      return middle_index

    # 4. if not equal, calculate arr[middle_index] - middle_index
    if (arr[middle_index] - middle_index) > 0:
      ceiling_index = middle_index
      continue

    # 4.1 if calculate arr[middle_index] - middle_index > 0, set ceiling_index == middle_index
    # 4.2 if calculate arr[middle_index] - middle_index < 0, set floor_index == middle_index
    if (arr[middle_index] - middle_index) < 0:
      floor_index = middle_index
      continue

  return -1


if __name__ == '__main__':
  case_1 = [-8,0,2,5]
  case_2 = [-1, 0, 3 ,6]
  case_3 = [-1]
  case_4 = []

  expected_1 = 2
  expected_2 = -1
  expected_3 = -1
  expected_4 = -1

  solution_1 = index_equals_value_search(case_1)
  solution_2 = index_equals_value_search(case_2)
  solution_3 = index_equals_value_search(case_3)
  solution_4 = index_equals_value_search(case_4)

  assert expected_1 == solution_1
  assert expected_2 == solution_2
  assert expected_3 == solution_3
  assert expected_4 == solution_4

