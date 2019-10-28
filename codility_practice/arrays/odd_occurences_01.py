# Odd occurences
# A non-empty array A consisting of N integers is given. The array contains an
# odd number of elements, and each element of the array can be paired with another
# element that has the same value, except for one element that is left unpaired.

# For example, in array A such that:

#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the elements at indexes 0 and 2 have value 9,
# the elements at indexes 1 and 3 have value 3,
# the elements at indexes 4 and 6 have value 9,
# the element at index 5 has value 7 and is unpaired.
# Write a function:

# class Solution { public int solution(int[] A); }

# that, given an array A consisting of N integers fulfilling the above conditions,
# returns the value of the unpaired element.

# For example, given array A such that:

#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the function should return 7, as explained in the example above.

# Write an efficient algorithm for the following assumptions:

# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.

# ================ solution ==============

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# 1. initialize a set
# 2. for each element in A,
# 3. check if element exists in set
#   3.1 if exists, then remove from set
#   3.2 if doesn't exist, the add to set
# 4. pop the element from set and return value
#
# has time complexity O(N) and spatial complexity of O(N)

def solution(A):
    if len(A) == 1:
        return A[0]

    # 1. initialize a set
    pairs_set = set()
    # 2. for each element in A,
    for element in A:
        # 3. check if element exists in set
        if element in pairs_set:

            #   3.1 if exists, then remove from set
            pairs_set.remove(element)
        else:
            #   3.2 if doesn't exist, the add to set
            pairs_set.add(element)

    # 4. pop the element from set and return value
    return pairs_set.pop()

    # has time complexity O(N) and spatial complexity of O(N)
