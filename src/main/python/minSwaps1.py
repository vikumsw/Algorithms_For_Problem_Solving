class Solution:
    def minSwaps(self, s: str) -> int:
        c1,c2 = 0,0
        for c in s:
            if c == '[': c1 += 1
            else:
                if c1>0:c1 -= 1
                else: c2 += 1

        return (c1+1)//2