import unittest

"""
Problem : 
Let's define a "sevenish" number to be one which is either a power of 7,
 or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on.
Create an algorithm to find the nth sevenish number.
"""

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(NthSevenish(1), 1)

    def test2(self):
        self.assertEqual(NthSevenish(2), 7)

    def test3(self):
        self.assertEqual(NthSevenish(3), 8)

    def test4(self):
        self.assertEqual(NthSevenish(4), 49)


def NthSevenish(n):
    pos = 1
    val = 0
    count = 0
    while n >= pos:
        if pos & n == pos:
            val += 7**count
        pos *= 2
        count += 1
    return val


if __name__ == '__main__':
    unittest.main()
