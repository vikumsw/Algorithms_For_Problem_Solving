class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mpb = 0
        for n in nums:
            mpb = mpb | n
        
        #print(mpb)
        
        l = len(nums)
        
        
        cnt = 0
        for i in range(2**l):
            cur = 0
            
            for k in range(l):
                if 1<<k & i:
                    cur = cur | nums[k]
            
            if cur == mpb:
                cnt = cnt + 1
                #print(i)
                
        return cnt