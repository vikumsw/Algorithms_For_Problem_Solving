import unittest

"""
Problem : 
This problem was asked by Oracle.
We say a number is sparse if there are no adjacent ones in its binary representation. For example, 21 (10101) is sparse, but 22 (10110) is not.
For a given input N, find the smallest sparse number greater than or equal to N.
Do this in faster than O(N log N) time.
"""


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(smallestSparseNumber(3), 4)

    def test2(self):
        self.assertEqual(smallestSparseNumber(8), 8)

    def test3(self):
        self.assertEqual(smallestSparseNumber(5), 5) #already sparse

    def test4(self):
        self.assertEqual(smallestSparseNumber(9), 9) #already sparse

    def test5(self):
        self.assertEqual(smallestSparseNumber(6), 8)


def smallestSparseNumber(val):
    pos = 1
    prev = False
    num = 0

    while pos <= val:
        if val & pos != 0:  # found 1
            if prev:  # found 1 and previous is also 1
                num = pos
                prev = True
            else:  # found 1 and previous is not 1
                num += pos
                prev = True
        else:
            prev = False

        pos *= 2

    if num < val:
        num = pos

    return num


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
