import unittest
import itertools

class AddrComboTest(unittest.TestCase):
    @staticmethod
    def test():
        print(parse("127345"))
        print(parse2("127345"))
        # print(parse("34765234"))
        print(parse2("2542540123"))


def parse(addr):
    ips = []

    for cmb_i in range(pow(3, 4)):
        adr = addr
        ip = []
        for _ in range(4):
            digits = cmb_i % 3 + 1
            val = adr[:digits]

            if len(val) < digits:
                break
            else:
                if not isvalid(val):
                    break

            ip.append(val)
            adr = adr[digits:]

            cmb_i = int(cmb_i/3)

        if len(adr) == 0 and len(ip) == 4:
            ips.append('.'.join(ip))

    return ips


def parse2(addr):
    ips = []

    for sel in itertools.product([1, 2, 3], repeat=4):
        if len(addr) == sum(sel):
            acc_sel = [0] + list(itertools.accumulate(sel))

            parts = [addr[i:j]
                     for i, j in zip(acc_sel, acc_sel[1:])
                     if isvalid(addr[i:j])]

            if len(parts) == 4:
                ips.append('.'.join(parts))

    return ips


def isvalid(node):
    return int(node) <= 255 and len(str(int(node))) == len(node)


# print(list(itertools.combinations_with_replacement(range(3), 4)))
# if __name__ == '__main__':
#     unittest.main()

