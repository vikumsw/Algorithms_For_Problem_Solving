class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        k = 0
        
        def isSubSeq(l):
            cnt=0
            good = [True for _ in range(len(s))]
            for r in l:
                good[r] = False
            for i in range(len(s)):
                if s[i]==p[cnt] and good[i]:
                    cnt+=1
                    if cnt==len(p):
                        return True
                    
            return False
        
        
        if len(removable)<1:
            return 0
        
        if isSubSeq(removable[:len(removable)]):
            return len(removable)
        
        if not isSubSeq(removable[:1]):
            return 0
        
        
        hi = len(removable)-1
        lo = 0
        while lo<hi:
            mid = lo + (hi-lo)//2
            
            if isSubSeq(removable[:mid+1]):
                lo = mid + 1
            else:
                hi = mid
            
        return lo
