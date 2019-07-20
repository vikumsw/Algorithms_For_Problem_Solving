import unittest


class Test(unittest.TestCase):
    def test1(self):
        assert maxones(167) == 3
        assert maxones(165) == 1
        assert maxones(57) == 3
        assert maxones(156) == 3


def maxones(val):
    cnt = 0
    maxcnt = 0

    while val > 0:
        cnt = cnt + 1 if val % 2 == 1 else 0

        maxcnt = max(maxcnt, cnt)
        val = int(val/2)

    return maxcnt


if __name__ == '__main__':
    unittest.main()
