class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c,mx = 0, 0
        for e in nums:
            if e==1:c+=1
            else:
                mx = max(mx,c)
                c=0
                
        mx = max(mx,c)
        return mx
        
