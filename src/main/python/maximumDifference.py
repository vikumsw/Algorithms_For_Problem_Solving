class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m=1000000005
        md=-1
        for e in nums:
            if e-m>md and e-m>0:md=e-m
            m=min(m,e)
            
        return md
        
