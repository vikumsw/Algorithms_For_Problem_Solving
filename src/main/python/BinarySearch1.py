class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(nums)
        
        lo = 0
        hi = len(nums)-1
        
        while lo<=hi:
            m = lo + (hi-lo)//2
            print(m)
            if nums[m] == target:
                return m
            elif nums[m]>target:
                hi = m-1
            else:
                lo = m+1
        
        return -1
