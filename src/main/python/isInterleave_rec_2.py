class Solution:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3 = len(s1),len(s2),len(s3)
        cache = [[-1 for _ in range(l2+1)] for _ in range(l1+1)]
        
        if l3 != l1+l2: return False
        
        def isInterleaveInner(i1,i2,i3):
            print((i1,i2,i3))
            ll1,ll2,ll3 = l1-i1,l2-i2,l3-i3
        
            if ll3 ==0 and (ll1>0 or ll2>0): return False

            if (ll1,ll2,ll3) == (0,0,0) : return True

            if cache[i1][i2]>= 0: return True if cache[i1][i2]==1 else False

            if ll1>0 and ll3>0 and s1[i1] == s3[i3]:
                if isInterleaveInner(i1+1, i2, i3+1):
                    cache[i1+1][i2] = 1
                    return True
                else:
                    cache[i1+1][i2] = 0

            if ll2 > 0 and ll3>0 and s2[i2] == s3 [i3]:
                if isInterleaveInner(i1, i2+1, i3+1):
                    cache[i1][i2+1] = 1
                    return True
                else:
                    cache[i1][i2+1] = 0
                
                
            
            return False
            
        return isInterleaveInner(0,0,0)
        
