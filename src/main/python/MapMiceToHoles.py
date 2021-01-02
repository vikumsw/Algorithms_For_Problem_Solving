#!/usr/bin/env python

"""
Challenge #725
Consider the following scenario: there are N mice and N holes placed at integer points along a line.
Given this, find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.

Each move consists of moving one mouse one unit to the left or right, and only one mouse can fit inside each hole.

For example, suppose the mice are positioned at [1, 4, 9, 15], and the holes are located at [10, -5, 0, 16].
In this case, the best pairing would require us to send the mouse at 1 to the hole at -5, so our function should return 6.
"""


def findlargeststeps(mice, holes):
    mice.sort()
    holes.sort()

    max_steps = 0
    for i in range(len(mice)):
        steps = abs(mice[i] - holes[i])
        if steps > max_steps:
            max_steps = steps
    return max_steps


mice = [1, 4, 9, 15]
holes = [10, -5, 0, 16]

print(findlargeststeps(mice, holes))

mice2 = [-10, -79, -79, 67, 93, -85, -28, -94]
holes2 = [2, 9, 69, 25, -31, 23, 50, 78]

print(findlargeststeps(mice2, holes2))
