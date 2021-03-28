class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        lo,hi = 0, l-1
        while lo<=hi:
            mid = lo + (hi - lo) // 2
            if target == nums[mid]:
                s = e = mid
                while s-1 >= 0 and nums[s-1] == target: s -= 1
                while e+1 <= l-1 and nums[e+1] == target: e += 1
                return [s,e]
            elif target < nums[mid]:
                hi = mid-1
            else:
                lo = mid+1
        return [-1,-1]