# Binary Gap
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
#
# ========= solution ==========
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# pseducode
#   1. convert N to binary number
#   2. acquire string without character at position 0 and position N-1
#   3. separate 0 from 1s
#   4. count number of zeros in list
#   5. return count
#
def solution(N):
    #   1. convert N to binary number
    binary = "{0:b}".format(N)

    #   2. acquire string without character at position 0 and position N-1
    #   3. separate 0 from 1s
    binary_zeros_list = binary.split('1')[1:-1]

    #   4. count number of zeros in list
    longest_binary_zero = get_longest_zero(binary, binary_zeros_list)

    #   5. return count
    return longest_binary_zero

def get_longest_zero(binary, binary_zeros_list):
    index = 0
    index_end = len(binary_zeros_list)
    longest_zeros = 0

    if binary[0] == 0:
        index = 1

    if binary[-1] == 0:
        index_end = index_end - 1

    if index >= index_end:
        return 0

    while index < index_end:
        zeros_length = len(binary_zeros_list[index])

        if zeros_length == 0:
            index += 1
            continue

        if zeros_length > longest_zeros:
            longest_zeros = zeros_length
        index += 1

    return longest_zeros

