class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        cur = 1
        
        while len(nums)> cur:
            if nums[cur] == nums[cur-1]:
                del nums[cur]
            else:
                cur +=1
        
        return len(nums)
                
