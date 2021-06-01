class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        
        if l == 1:
            return 0
        
        lo = 0
        hi = l-1
        while lo<=hi:
            mid = lo + (hi - lo) // 2
            if (0<mid<l-1 and nums[mid-1]<nums[mid]>nums[mid+1]) or (mid==0 and nums[mid] > nums[mid+1]) or (mid==l-1 and nums[mid]>nums[mid-1]):
                return mid
            elif (mid>0 and nums[mid-1]>nums[mid]>nums[mid+1]) or (mid==l-1 and nums[mid] < nums[mid-1]):
                hi = mid - 1
            elif (nums[mid-1]<nums[mid]<nums[mid+1]) or (mid==0 and nums[mid] < nums[mid+1]):
                lo = mid+1
            else:
                hi = mid - 1
            
        return -1
