class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        l=len(s)
        
        cache = [-1 for _ in range(l)]
        cache[0] = 1
        def canReachIndex(idx):
            if s[idx]=='1':return False
            if cache[idx]!=-1: return (True if cache[idx]==1 else False)
            
            upper = max(idx - minJump + 1,0)
            lower = max(idx - maxJump,0)
            
            for j in range(lower,upper):
                if canReachIndex(j):
                    cache[j] = 1
                    return True
                else:
                    cache[j] = 0
            
            print(cache)
            cache[idx]=0
            return False
                    
        return canReachIndex(l-1)
