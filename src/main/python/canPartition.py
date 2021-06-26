class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot%2==1:return False
        tar = sum(nums)/2
        cache = {}
        
        def canFindSubset(n,t):
            if n==0 and t==0: return True
            if n==0 and t>0:return False
            if t < 0 : return False 
            
            if (n,t) in cache:
                return cache[(n,t)]
            
            if canFindSubset(n-1,t):
                cache[(n-1,t)] = True
                return True
            else:
                cache[(n-1,t)] = False
                
            if canFindSubset(n-1,t-nums[n-1]):
                cache[(n-1,t-nums[n-1])] = True
                return True
            else:
                cache[(n-1,t-nums[n-1])] = False
                
            return False
        
        return canFindSubset(len(nums),tar)
