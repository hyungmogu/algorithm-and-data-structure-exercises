# Tie Ropes
#
# Given an array of intergers A, and threshold rope length K (integer),
# find maximum number of ropes that is greater than or equal to K
#
# two adjacent ropes A[index] and A[index - 1] can be tied together
#
# input
#   - list of integers
#   - integer
#
# output
#   - intger (total number of ropes with length greather than or equal to K)
#
# constraints
#   - N is the size of list in range [1 ... 100,000]
#   - K is integer in between [1 ... 1,000,000,000,000]
#   - each element of array A is within the range [1 ... 1,000,000,000]
#
# Example
#
# [1,2,3,4,1,1,3] K = 4
#
# |--1--||----- 2 -----||------3------||--------4--------||--1--||--1--||------3-------|
#
#  | ---------- 1 --------------------||--------2--------||-----------3 ---------------|
#
#
# output: 3
#
# cases
#   1. K == 1 <- return len(A)
#   2. K != 1
#
# Brainstorming solution
# 0. if K == 1, return len(A)
# 1. initialize index, rope_length and count to be 0
# 2. while index < len(A)
# 3. Add A[index] to 'rope_length' <-- current rope total
# 4. if rope_length >= K:
#   3.1 raise count by 1
#   3.2 reset rope_length = 0
# 5. return count
#
# time complexity O(N) and spatial complexity O(1)


class Solution:
    def solve(self, K, A):
        # 0. if K == 1, return len(A)
        if K == 1:
            return len(A)

        # 1. initialize index, rope_length and count to be 0
        index = rope_length = count = 0

        # 2. while index < len(A)
        while index < len(A):
            # 3. Add A[index] to 'rope_length' <-- current rope total
            rope_length += A[index]

            # 4. if rope_length >= K:
            if rope_length >= K:
                #   3.1 raise count by 1
                count += 1
                #   3.2 reset rope_length = 0
                rope_length = 0

            index +=1
        # 5. return count
        return count

if __name__ == '__main__':
    A_case_1 = [1,2,3,4,1,1,3]
    K_case_1 = 4

    expected_1 = 3

    solution_1 = Solution().solve(K_case_1, A_case_1)

    assert expected_1 == solution_1