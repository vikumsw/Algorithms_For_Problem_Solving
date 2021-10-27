class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i,e in enumerate(nums):
            if i%10 == e:
                return i
            
        
        return -1
        