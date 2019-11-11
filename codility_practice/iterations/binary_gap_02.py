# Binary Gap
# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
#
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
# ================= solution =======================
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
# goal
#    -> find the longest binary number
#
# input
#   - integer
#
# output
#   - integer
#
# constraint
#   - N is an integer between [1 ... 2,147,483,647]
#
#
# 529 --> 1000010001 --> 00001000 --> '0000','000'
#
# cases
#   1. when there is no 1 at the end --> don't count
#   2. where there is no 1 at the front --> don't count
#   3. when there are many 1s in between --K skip
#
# Pseudocode
# 1. convert N to binary number
# 2. strip out 1 at the beginning and the end
# 3. split by 1
# 4. if there is no 1 at the end, reduce upper bound or 'index_end' from N to N-1
# 5. if there is no 1 at the front, set 1 to be 1
# 6. for each value,
# 7. if number is empty, then skip
# 8. if not empty, compare and evaluate the lengthiest value of 0
# 9. return value

def solution(N):
    # 1. convert N to binary number
    binary = '{0:b}'.format(N)
    largest_zeros = 0
    # 2. strip out 1 at the beginning and the end
    # 3. split by 1
    zeros_list = binary[1:-1].split('1')

    index = 0
    index_end = len(zeros_list)

    # 4. if there is no 1 at the end, reduce upper bound or 'index_end' from N to N-1
    if binary[0] != '1':
        index += 1

    # 5. if there is no 1 at the front, set 1 to be 1
    if binary[-1] != '1':
        index_end -= 1

    # 6. for each value,
    while index < index_end:
        value = zeros_list[index]

        # 7. if number is empty, then skip
        if value == '':
            index += 1
            continue
        # 8. if not empty, compare and evaluate the lengthiest value of 0
        largest_zeros = max(largest_zeros, len(value))

        index += 1
    # 9. return value

    return largest_zeros

