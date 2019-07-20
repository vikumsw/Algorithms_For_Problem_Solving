import unittest


class Test(unittest.TestCase):
    def test(self):
        assert excel_num2column(27) == 'AA'
        assert excel_num2column(1) == 'A'


def excel_num2column(val):
    outstr = ''

    while val > 0:
        c = chr((val - 1) % 26 + ord('A'))
        outstr = c + outstr
        val = int(val/26)

    return outstr


if __name__ == '__main__':
    unittest.main()
