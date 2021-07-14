class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        while p < len(nums):
            if nums[p] == val:
                nums.pop(p)
            else:
                p+=1
                
        return len(nums)