class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        
        if l == 1:
            return 0
        
        lo = 0
        hi = l-1
        while lo<hi:
            mid = lo + (hi - lo) // 2
            if nums[mid]>nums[mid+1]:
                hi = mid
            elif nums[mid]<nums[mid+1]:
                lo = mid+1
            
        return lo
