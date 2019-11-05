# Odd occurences
# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

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

# ================= solution ================
#
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# problem: array contains odd number of elements, and each
# element of the array can be paired with another
#
# given list of array, return the value of unpaired elemenet
#
# pseudocode
def solution(A):
    #   1. Initialize set
    pairs_set = set()

    #   2. for each element in A
    for element in A:

    #   3. if check if element exists in a set
    #   4. if element doesn't exist, add to set
    #   5. if elemenet does exist, remove from set

        if not element in pairs_set:
            pairs_set.add(element)

    #   6. return the last element
        else:
            pairs_set.remove(element)

    unpaired_value = pairs_set.pop()


    return unpaired_value

