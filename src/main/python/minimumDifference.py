class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sz = len(nums)
        nums.sort()
        cm = 100005
        si = 0
        ei = k-1
        
        while ei<sz:
            tm = nums[ei] - nums[si]
            if tm < cm: cm = tm
            si += 1
            ei += 1 
        
        return cm