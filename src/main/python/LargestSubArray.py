import unittest

"""
Problem : 
Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
"""


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, 6, "Should be 6")

    def test2(self):
        arr = [1,-1, 2, -3, -4, 5, 6, 7]
        self.assertEqual(maximumSubArraySum(arr), 8, "Should be 8")

    def test3(self):
        arr = [1, 2, -3, -4, 5]
        self.assertEqual(maximumSubArraySum(arr), 8, "Should be 8")


def maximumSubArraySum(arr=[]):
    largest = arr[0]
    length = len(arr)
    i = 0
    subarraysum = arr[0]
    while i < length:
        #print(arr[i])
        current = arr[i]
        if arr[i] < 0:
            j = i+1
            while j < length and arr[j] < 0:
                i = j
                current = current + arr[j];
                j = j+1
            print(current)
            largest = getLargest(largest, current)
        else:
            j = i + 1
            while j < length and arr[j] > 0:
                i = j
                current = current + arr[j]
                j = j + 1
            print(current)
            largest = getLargest(largest, current)



        i = i+1
    print(largest)


def getLargest(l, val):
    if l < val:
        return val
    else:
        return l


if __name__ == '__main__':
    unittest.main()
