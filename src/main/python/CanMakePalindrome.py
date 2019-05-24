import unittest

"""
Problem : 
This problem was asked by Amazon.
Given a string, determine whether any permutation of it is a palindrome.
For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
daily should return false, since there's no rearrangement that can form a palindrome.
"""


class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(canMakePalindrome("aabb"))

    def test2(self):
        self.assertFalse(canMakePalindrome("aabbwk"))

    def test3(self):
        self.assertTrue(canMakePalindrome("aabba"))


def canMakePalindrome(string):
    a = Map()
    oddCharacterCount = 0
    for c in string:
        a[c] += 1
        if isEven(a[c]):
            oddCharacterCount -= 1
        else:
            oddCharacterCount += 1

    if oddCharacterCount < 2:
        return True

    return False


def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


class Map(dict):
    def __missing__(self, key):
        return 0


if __name__ == '__main__':
    unittest.main()
