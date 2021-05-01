class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        elif x <= 3:
            return 1
        
        l = 2
        h = x/2
        
        while l<=h:
            m = l + (h-l)//2
            p2 = m**2
            p3 = (m+1)**2
            if p2==x or (p2<x<p3):
                return int(m)
            elif p2>x:
                h = m-1
            else:
                l = m+1
            
        return -1