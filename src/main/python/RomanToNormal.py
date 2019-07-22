import unittest


class RomanToNormalTest(unittest.TestCase):

    def test(self):
        assert roman2normal('IX') == 9
        assert roman2normal('XIII') == 13
        assert roman2normal('XLI') == 41
        assert roman2normal('MCDXXXV') == 1435
        assert roman2normal('XIV') == 14


rndata = {'M': 1000, 'D': 500, 'C':100, 'L': 50, 'X': 10, 'V':5, 'I': 1}


def roman2normal(val):
    total = 0
    pre_digit = 0

    for ch in val:
        digit = rndata[ch]
        total += digit
        if pre_digit < digit:
            total -= pre_digit*2
        pre_digit = digit

    return total

