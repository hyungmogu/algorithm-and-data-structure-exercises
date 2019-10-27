# Min Max Division
#
# You are given integers K, M and a non-empty array A consisting of N integers.
# Every element of the array is not greater than M.
#
# You should divide this array into K blocks of consecutive elements. The size
# of the block is any integer between 0 and N. Every element of the array should
# belong to some block.
#
# The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum
# of empty block equals 0.
#
# The large sum is the maximal sum of any block.
#
# For example, you are given integers K = 3, M = 5 and array A such that:
#
#   A[0] = 2
#   A[1] = 1
#   A[2] = 5
#   A[3] = 1
#   A[4] = 2
#   A[5] = 2
#   A[6] = 2
# The array can be divided, for example, into the following blocks:
#
# [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
# [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
# [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
# [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
# The goal is to minimize the large sum. In the above example, 6 is the minimal
# large sum.
#
# Write a function:
#
# def solution(K, M, A)
#
# that, given integers K, M and a non-empty array A consisting of N integers,
# returns the minimal large sum.
#
# For example, given K = 3, M = 5 and array A such that:
#
#   A[0] = 2
#   A[1] = 1
#   A[2] = 5
#   A[3] = 1
#   A[4] = 2
#   A[5] = 2
#   A[6] = 2
# the function should return 6, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N and K are integers within the range [1..100,000];
# M is an integer within the range [0..10,000];
# each element of array A is an integer within the range [0..M].

# ============================

# Problem
#   - given K many partitions and (M - 1) maximal number of elements in the paritioned
#   block, design an algorithm that evaluates the lowest large sum of a
#   partitioned block
#
# Input
#   - list of integers (A)
#   - integer (K - number of paritions)
#   - integer (M - upper bound of number of elements in partitioned block)
#
# Output
#   - integer (smallest largest sum)
#
# Example
#
# Before partition
#
# K = 3, M = 5
# [2,1,5,1,2,2,2][][] largest sum = 15
#
# partition #1
# [2][1,5,1,2,2][2] --> second block exceeds M --> [2][1,5,1,2][2,2] ==> large sum 9
#
# partition #2
#
# [2][1,5,1,2][2,2] - >[2,1,5][][1,2,2,2] largest sum = 8
#
#
# parition # 3
# [2,1,5][][1,2,2,2] --> [2, 1][5, 1][2, 2, 2] largest sum = 6
#
# partition # 4
# [2][1,5,1,2][2,2] largest sum 9 --> here we stop!
#
# pseudocode
# 1. calculate initial sum
# 2. initialize paritiion
# 3. while solution not found
# 4. find the largest sum in partition
# 5. if is not solution
# 6. reparition the block

def solution(K, M, A):
    large_sum = sum(A)
    current_sum = 0
    paritions = initialize_parition(A,K,M)

    # 3. while solution not found
    while True:
        # 4. find the largest sum in partition
        large_sum = get_large_sum(A, partitions)
        # 5. if is not solution
        if current_sum <= large_sum:
            large_sum = current_sum
            partitions = update_partition(A, parititions)
        # 6. reparition the block
        else:
            break

    return large_sum

# =============
# - find the half distance of adjacent matrix
# - move its limit by the amount
#   - pointers on left to right
#   - last pointer to left
#   - if two pointers cross, switch direction
