import unittest

"""
Problem : 
Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.
"""

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(maxMin([3, 12, 8, 13]), [3, 13, 5])

    def test2(self):
        self.assertEqual(func(2, 2), 4)

    def test3(self):
        self.assertTrue(maxMin([3, 12, 8, 13])[0:2] == [3, 13] and maxMin([3, 12, 8, 13])[2] < 6)


def func(a, b):
    return a + b


def maxMin(arr=[]):
    max = arr[0]
    min = arr[0]
    compCount = 0
    for i in range(len(arr)-1):
        ele = arr[i+1]
        temp = (max-ele) * (min-ele)
        if temp > 0:
            compCount += 1
            if max < ele:
                max = ele
            else:
                min = ele
        compCount += 1

        print(ele + 1, ' ', temp)

    return [min, max, compCount]

if __name__ == '__main__':
    unittest.main()






"""
.assertEqual(a, b)  	    a == b
.assertTrue(x)      	    bool(x) is True
.assertFalse(x)	            bool(x) is False
.assertIs(a, b)	            a is b
.assertIsNone(x)	        x is None
.assertIn(a, b)	            a in b
.assertIsInstance(a, b)	    isinstance(a, b)
"""