class Solution:
    def findGCD(self, nums: List[int]) -> int:
        sml = min(nums)
        lrg = max(nums)
        
        for i in range(sml):
            d = sml - i
            if sml%d == 0 and lrg%d==0:
                return d
        
        return 1