# Fish

# You are given two non-empty arrays A and B consisting of N integers. Arrays A
# and B represent N voracious fish in a river, ordered downstream along the flow
# of the river.

# The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then
# fish P is initially upstream of fish Q. Initially, each fish has a unique position.

# Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the
# fish. All its elements are unique. Array B contains the directions of the fish.
# It contains only 0s and/or 1s, where:

# 0 represents a fish flowing upstream,
# 1 represents a fish flowing downstream.
# If two fish move in opposite directions and there are no other (living) fish
# between them, they will eventually meet each other. Then only one fish can stay
# alive − the larger fish eats the smaller one. More precisely, we say that two
# fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are
# no living fish between them. After they meet:

# If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
# If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
# We assume that all the fish are flowing at the same speed. That is, fish moving
# in the same direction never meet. The goal is to calculate the number of fish
# that will stay alive.

# For example, consider arrays A and B such that:

#   A[0] = 4    B[0] = 0
#   A[1] = 3    B[1] = 1
#   A[2] = 2    B[2] = 0
#   A[3] = 1    B[3] = 0
#   A[4] = 5    B[4] = 0
# Initially all the fish are alive and all except fish number 1 are moving upstream.
# Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats
# it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish,
# number 0 and 4, never meet and therefore stay alive.

# Write a function:

# def solution(A, B)

# that, given two non-empty arrays A and B consisting of N integers, returns the
# number of fish that will stay alive.

# For example, given the arrays shown above, the function should return 2, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [0..1,000,000,000];
# each element of array B is an integer that can have one of the following values: 0, 1;
# the elements of A are all distinct.


#=========== solution =========

# you can write to stdout for debugging purposes, e.g.
# print

# inputs
#   - list of integers (A - representing fishses size)
#   - list of integers (B - representing fish type & direction)
#
# output
#   - integers (number of fish that stays alive)
#
# known
#   - red fish represented by 1, travels west
#   - blue fish represented by 0, travels east
#
#   - if SIZE[red_fish] > SIZE[blue_fish], blue_fish gets eaten by red fish
#   - if SIZE[red_fish] < SIZE[blue_fish], red_fish gets eaten by blue fish
#   - if SIZE[red_fish] == SIZE[blue_fish], no fish dies
#
#   -
#
# constraint
#   - N, size of A and B is in between [1 ... 100,000]
#   - element in array A is within range [0 ... 1,000,000,000]
#   - element in array B is either 0 or 1
#   - all elements in A are distinct
#
# case
#   1. N of A and B == 1  --> return 0
#   2. N of A and B != 1

# pseudocode
#   1. while index < N
#   2. if B[index] is red fish,
#       2.1 push to stack with its size A[index]
#
#   3.if B[index] is blue fish
#       2.1 peak stack (the latest red fish)
#       2.2 if stack empty, continue
#       2.2 if SIZE[Red_fish] > SIZE[Blue_fish], raise death count by 1
#       2.3 if SIZE[blue_fish] > SIZE[red_fish], raise death count by 1, pop stack
#       2.4 if SIZE[blue_fish] == SIZE[red_fish], continue
#
#   4. return N - death_count

# time complexity O(N) and spatial complexity O(N)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):

        if len(self.items) == 0:
            return None

        return self.items.pop()

    def peak(self):
        if len(self.items) == 0:
            return None

        return self.items[-1]

    def size(self):
        return len(self.items)

def solution(A, B):
    N = len(A)
    death_count = 0
    index = 0
    red_fishes_stack = Stack()

    #   1. while index < N
    while index < N:
        #   2. if B[index] is red fish,
        if B[index] == 1:
            #       2.1 push to stack with its size A[index]
            red_fishes_stack.push(A[index])

        #   3.if B[index] is blue fish
        else:
            #       2.0 if stack empty, continue
            if red_fishes_stack.size() == 0:
                index += 1
                continue

            while red_fishes_stack.size() > 0:
                #       2.1 peak stack (the latest red fish)

                red_fish_size = red_fishes_stack.peak()
                blue_fish_size = A[index]

                #       2.2 if SIZE[Red_fish] > SIZE[Blue_fish], raise death count by 1
                if red_fish_size > blue_fish_size:
                    death_count += 1
                    break

                #       2.3 if SIZE[blue_fish] > SIZE[red_fish], raise death count by 1, pop stack
                elif red_fish_size < blue_fish_size:
                    death_count += 1
                    red_fishes_stack.pop()

                #       2.4 if SIZE[blue_fish] == SIZE[red_fish], continue

        #   4. increment
        index += 1

    return N - death_count


if __name__ == '__main__':
    A_case_1 = [4,3,2,1,5]
    B_case_1 = [0,1,0,0,0]

    expected_1 = 2

    solution_1 = solution(A_case_1, B_case_1)

    assert expected_1 == solution_1
