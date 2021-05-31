class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        
        #find s
        lo,hi = 0, l-1
        s = -1
        while lo<=hi:
            mid = lo + (hi - lo) // 2
            print("s:"+str(mid))
            if (target == nums[mid] and mid > 0 and target > nums[mid-1]) or (target == nums[mid] and mid==0):
                s = mid
                break
            elif (target == nums[mid] and mid > 0 and target == nums[mid-1]) or target < nums[mid]:
                #go low
                hi = mid-1
            elif target > nums[mid]:
                #go high
                lo = mid+1
        
        #find e
        lo,hi = 0, l-1
        e = -1
        while lo<=hi:
            mid = lo + (hi - lo) // 2
            print("s:"+str(mid))
            if (target == nums[mid] and mid < l-1 and target < nums[mid+1]) or (target == nums[mid] and mid==l-1):
                e = mid
                break
            elif target < nums[mid]:
                #go low
                hi = mid-1
            elif (target == nums[mid] and mid < l-1 and target == nums[mid+1]) or target > nums[mid]:
                #go high
                lo = mid+1
                
        return [s,e]
