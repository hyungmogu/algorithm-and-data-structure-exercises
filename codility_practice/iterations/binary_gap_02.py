# Binary Gap
# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
#
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

