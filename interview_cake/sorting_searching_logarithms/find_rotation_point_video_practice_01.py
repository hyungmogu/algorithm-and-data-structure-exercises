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
#
# word = [
#     'ptolemaic', # top
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',
#     'bear'
# ]
#
# word = [
#     'ptolemaic', # top
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',
# ]
#
#
#
# input
#   list of string
#
# output
#   index of rotation point (intger)
#


# Uses binary search algorithm. Has time complexity of O(log N) and spatial complexity of O(1)

class Solution:
    def rotationPoint(self, words):
        floor_index = -1
        ceiling_index = len(words)

        # 1. find the middle point
        half_distance = (ceiling_index - floor_index) / 2
        guess_index = floor_index + half_distance

        # 2. check and see if the middle point is solution
        # 3. if solution, return index
        if self.is_solution(words, guess_index):
            return guess_index

        # 4. otherwise, and if solution exists top, then set ceiling_index = guess_index
        if self.solution_exists_top(words, guess_index):
            ceiling_index = guess_index

        # 5. othwersie, and if solution exists bottom, then set floor_index = guess_index
        if self.solution_exists_bottom(words, guess_index):
            floor_index = guess_index


    def is_solution(self, words, guess_index):
        if (guess_index + 1 == len(words) and
            words[guess_index - 1] > words[guess_index] and
            words[0] > words[guess_index]):

            return True

        if (words[guess_index - 1] > words[guess_index] and
            words[guess_index + 1] > words[guess_index]):

            return True

        # 1. no words with smaller order index

    def solution_exists_top(self, words, guess_index):

        if (words[guess_index - 1] < words[guess_index] and
            words[guess_index + 1] > words[guess_index]):

            return True

    def solution_exists_bottom(self, words, guess_index):

        if (words[-1] < words[0]):
            return True

        if (words[guess_index + 1] < words[guess_index]):
            return True


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

    expected = 5

    solution = Solution().rotationPoint(case)

    assert expected == solution