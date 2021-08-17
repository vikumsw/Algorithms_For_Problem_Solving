class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        mi = 5000
        vis = [False]*5000
        vis[0] = True
        for r in mat:
            temp = [False]*5000
            for i in range(5000):
                if vis[i]:
                    for c in r:
                        temp[i+c] = True
            
            vis = temp
        
        for i in range(5000):
            if vis[i]:
                m = abs(i-target)
                if mi>m:mi=m
                
        return mi