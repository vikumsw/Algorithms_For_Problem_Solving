import unittest


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_min([9, 23, 47, 2, 3, 6]), 2)

    def test2(self):
        self.assertEqual(find_min([5, 6, 8, 9, 13]), 5)

    def test3(self):
        self.assertEqual(find_min([15, 5, 6, 8, 9, 13]), 5)

    def test4(self):
        self.assertEqual(find_min([6, 8, 9, 13, 5]), 5)

    def test5(self):
        self.assertEqual(find_min([6, 8]), 6)

    def test6(self):
        self.assertEqual(find_min([8, 6]), 6)

    def test7(self):
        self.assertEqual(find_min([]), 0)

    def test8(self):
        self.assertEqual(find_min([8]), 8)

        
def find_min(data):
    if len(data) == 0:
        return 0

    if len(data) == 1:
        return data[0]

    return f_min(data, 0, len(data) - 1)


def f_min(data, start, end):
    if end - start == 1:
        return min(data[start], data[end])

    mid = start + int((end - start)/2)
    if(data[mid + 1] > data[mid]) and (data[mid - 1] > data[mid]):
        return data[mid]

    if(data[start] < data[mid]) and (data[end] < data[mid]):
        return f_min(data, mid, end)
    else:
        return f_min(data, start, mid)
