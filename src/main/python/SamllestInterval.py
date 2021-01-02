import unittest

"""
Challenge #723
This problem was asked by Google.
Given a set of closed intervals, find the smallest set of numbers that 
covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], 
one set of numbers that covers all these intervals is {3, 6}.
"""


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_smallest_range([[0, 3], [2, 6], [3, 4], [6, 9], [1, 2]]), (2, 6))

    def test2(self):
        self.assertEqual(find_smallest_range([[2, 3], [11, 23], [3, 6], [15, 16]]), (3, 15))

    def test3(self):
        self.assertEqual(find_smallest_range([[0, 30], [2, 3], [11, 23], [3, 6], [15, 16]]), (3, 15))

    def test4(self):
        self.assertEqual(find_smallest_range([[3, 6], [8, 11], [15, 21], [24, 30]]), (6, 24))


def find_smallest_range(intervals):
    intervals.sort(key=lambda x: x[0])
    lower, upper = intervals[0][1], intervals[len(intervals) - 1][0]
    for i in range(len(intervals) - 1):
        if intervals[i][1] < lower:
            lower = intervals[i][1]

    return lower, upper


if __name__ == '__main__':
    unittest.main()
