# Binary Gap
# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
#
# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at
# both ends in the binary representation of N.
#
# For example, number 9 has binary representation 1001 and contains a binary gap
# of length 2. The number 529 has binary representation 1000010001 and contains
# two binary gaps: one of length 4 and one of length 3. The number 20 has binary
# representation 10100 and contains one binary gap of length 1. The number 15
# has binary representation 1111 and has no binary gaps. The number 32 has
# binary representation 100000 and has no binary gaps.
#
# Write a function:
#
# def solution(N)
#
# that, given a positive integer N, returns the length of its longest binary gap.
# The function should return 0 if N doesn't contain a binary gap.
#
# For example, given N = 1041 the function should return 5, because N has binary
# representation 10000010001 and so its longest binary gap is of length 5.
# Given N = 32 the function should return 0, because N has binary representation
# '100000' and thus no binary gaps.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..2,147,483,647].
#
# ================= solution ====================
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal
#   - given an integer N, find the largest 0s in binary number
#
# input
#   - integer, N
#
# output
#   - integer (the lengthiest zero in N)
#
# constraints
#   - N is an integer between [1 ... 2,147,483,647]
#
# known
#   - only zeros in between 1s are considered
#       - "000" in "0001001" is not considered
#       - "00" in "1000100" is not considered
#   - {0:b}.format(N) converts number to a binary string

# Example
#   529 --> 1000010001
#   output: 4
#
# cases
#   1. when there is no 1 at the front --> ignore first zeros --> index += 1
#   2. when there is no 1 at then end --> ignore the last zeros --> index_end -= 1
#   3. when there is no 1 in between --> ignore empty zero
#       - '11111111'
#
# brainstorming solution
#   529 --> 1000010001 --> strip 1s at the end, and split by 1 --> ['0000','000'] --> get max
#    x  --> 11000010001 --> strip 1s at the end, and split by 1 --> ['','0000','000'] --> get max
#
#   1. convert N to binary number
#   2  strip 1s at the end and split by 1
#   3. if there is no 1 at the front, increment index by 1
#   4. if there is no 1 at the end, decrement index_end by 1
#   5. for each zeros in A,
#   6. if length zeros is 0, then skip
#   7. compare the largest_zeros with current zeros, and update the value of largest_zeros
#
#   8. return largest_zeros
#
#   Time complexity is O(N) and spatial complexity O(N)

def solution(N):
    #   1. convert N to binary number
    binary = '{0:b}'.format(N)
    #   2  strip 1s at the end and split by 1
    zeros_list = binary[1:-1].split('1')
    index = 0
    index_end = len(zeros_list)
    largest_zeros = 0

    #   3. if there is no 1 at the front, increment index by 1
    if binary[0] != '1':
        index += 1
    #   4. if there is no 1 at the end, decrement index_end by 1
    if binary[-1] != '1':
        index_end -= 1

    #   5. for each zeros in A,
    while index < index_end:
        zeros = zeros_list[index]
        #   6. if length zeros is 0, then skip
        if len(zeros) == 0:
            index += 1
            continue

        #   7. compare the largest_zeros with current zeros, and update the value of largest_zeros
        largest_zeros = max(largest_zeros, len(zeros))

        index += 1

    #   8. return largest_zeros
    return largest_zeros
