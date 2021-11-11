class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        hi = num
        lo = 1

        while lo<=hi:
            mid = lo + (hi-lo)//2
            
            squre = mid**2
            if squre==num:
                break
            elif squre>num:
                hi = mid - 1
            else:
                lo = mid + 1
        
        if mid**2 == num:return True
        
        return False
                
        