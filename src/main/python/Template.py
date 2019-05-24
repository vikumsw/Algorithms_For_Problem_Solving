import unittest

"""
Problem : 
This problem was asked by Amazon.
Given a string, determine whether any permutation of it is a palindrome.
Given a string, determine whether any permutation of it is a palindrome.
Given a string, determine whether any permutation of it is a palindrome.
"""

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(func(1, 2), 3)

    def test2(self):
        self.assertEqual(func(2, 2), 4)


def func(a, b):
    return a + b


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