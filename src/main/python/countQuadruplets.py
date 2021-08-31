class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ll = len(nums)
        count = 0
        for i in range(0,ll-3):
            for j in range(i+1,ll-2):
                for k in range(j+1,ll-1):
                    res = nums[i]+ nums[j]+ nums[k]
                    count +=  nums[k+1:].count(res)
        return count