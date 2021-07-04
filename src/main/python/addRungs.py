class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        def canClimb(cur,nextRungHeight):
            if cur + dist >= nextRungHeight:
                return True
            return False
            
        cur = 0
        count = 0
        ind = 0
        
        while ind < len(rungs):
            addRungs =  (rungs[ind] - cur - 1)//dist
            cur = rungs[ind]
            count+=addRungs
            ind+=1
                
        return count