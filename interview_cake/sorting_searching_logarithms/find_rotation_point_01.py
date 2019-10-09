# Find Rotation Point
#
# I want to learn some big words so people think I'm smart.
#
# I opened up a dictionary to a page in the middle and started flipping through,
# looking for words I didn't know. I put each word I didn't know at increasing
# indices in a huge list I created in memory. When I reached the end of the
# dictionary, I started from the beginning and did the same thing until I
# reached the page I started at.
#
# Now I have a list of words that are mostly alphabetical, except they start
# somewhere in the middle of the alphabet, reach the end, and then start from the
# beginning of the alphabet. In other words, this is an alphabetically ordered
# list that has been "rotated." For example:
#
#
#   words = [
#     'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',  # <-- rotates here!
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage',
# ]
#
# Write a function for finding the index of the "rotation point," which is where
# I started working from the beginning of the dictionary. This list is huge
# (there are lots of words I don't know) so we want to be efficient here.
#
#
# input
#   list of string
#
# output
#   index of rotation point (intger)
#
# Iteration #1
# words = [
#     'ptolemaic', #top
#     'retrograde',
#     'supplant',
#     'undulate', # has lesser order index
#     'xenoepist', # <-- this word order index feels like is at the peak
#     'asymptote', # has lesser order index
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage', # bottom
# ]


# Iteration #2
# words = [
#     'ptolemaic', # top
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',
#     'babka', # has lesser order index
#     'banoffee', # <-- This word order index feels like is at a slope
#     'engender', # has greater order index
#     'karpatka',
#     'othellolagkage', # bottom
# ]


# Iteration #2
# words = [
#     'ptolemaic', # top
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist', # has grater order index
#     'asymptote', # <-- this word order index feels like is at a valley
#     'babka', # has greater order index
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage', # bottom
# ]

# PSEUDOCODE
# floor_index = -1
# ceiling_index = len(words)
# # 1. while the binary search has not reached the end condition (floor_index and ceiling index don't cross)
# # 2. find the half point / guess index
# while not reached_the_end(floor_index, ceiling_index):

#     half_distance = (ceiling_index - floor_index) / 2
#     guess_index = floor_index + half_distance

# # 3. check if guess is solution (that is, the word's order of index has word with greater value / wall on both top and bottom)
#     if is_solution(words, guess_index):
#         return guess_index

# # 4. if not solution, and is at peak, set floor_index = guess_index
#     if at_peak(words, guess_index):
#         floor_index = guess_index
#         continue
# # 5. if not solution, and is slanted with lesser order index on top, set ceiling_index = guess_index
#     if at_slope(words, guess_index) and is_slanted_downward(words, guess_index):
#         ceiling_index = guess_index
#         continue
# # 6. if not solution, and is slanted with greater order index on top, set floor_index = guess_index
#     if at_slope(words, guess_index) and is_slatned_upward(words, guess_index):
#         floor_index = guess_index
#         continue

# Uses binary search algorithm. Has time complexity of O(log N) and spatial complexity of O(1)

class Solution:
    def rotationPoint(self, words):
        floor_index = -1
        ceiling_index = len(words)
        # 1. while the binary search has not reached the end condition (floor_index and ceiling index don't cross)
        # 2. find the half point / guess index
        while not self.reached_the_end(floor_index, ceiling_index):

            half_distance = (ceiling_index - floor_index) / 2
            guess_index = floor_index + half_distance

        # 3. check if guess is solution (that is, the word's order of index has word with greater value / wall on both top and bottom)
            if self.is_solution(words, guess_index):
                return words[guess_index]

        # 4. if not solution, and is at peak, set floor_index = guess_index
            if self.lesser_word_order_index_both_sides(words, guess_index):
                floor_index = guess_index
                continue

        # 5. if not solution, and is slanted with greater order index on top, set ceiling_index = guess_index
            if self.lesser_word_order_index_at_bottom(words, guess_index):
                ceiling_index = guess_index
                continue

        # 6. if not solution, and is slanted with greater order index on bottom, set floor_index = guess_index
            if self.lesser_word_order_index_at_top(words, guess_index):
                floor_index = guess_index
                continue

    def reached_the_end(self, floor_index, ceiling_index):
        if floor_index + 1 > ceiling_index:
            return True
        return False

    def is_solution(self, words, guess_index):
        # 1. is solution when it has reached the wall
        if guess_index == 0 or guess_index == len(words) - 1:
            return True

        # 2. is solution when is at a valley (words with greater order index on both sides)
        if (words[guess_index - 1] > words[guess_index] and
            words[guess_index + 1] > words[guess_index]):

            return True

    def lesser_word_order_index_both_sides(self, words, guess_index):
        try:
            if (words[guess_index - 1] < words[guess_index] and
                words[guess_index + 1] < words[guess_index]):
                return True
        except Exception:
            return False

    def lesser_word_order_index_at_bottom(self, words, guess_index):
        try:
            if (words[guess_index + 1] < words[guess_index]):
                return True
        except Exception:
            return False

    def lesser_word_order_index_at_bottom(self, words, guess_index):
        try:
            if (words[guess_index - 1] < words[guess_index]):
                return True
        except Exception:
            return False


if __name__ == '__main__':
    case = [
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'xenoepist',
        'asymptote',
        'babka',
        'banoffee',
        'engender',
        'karpatka',
        'othellolagkage',
    ]

    expected = 'asymptote'

    solution = Solution().rotationPoint(case)

    assert expected == solution