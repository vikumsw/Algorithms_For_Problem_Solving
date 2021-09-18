class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        b = 0
        ll=len(nums)
        
        end = [0 for _ in range(ll)]
        end[0]=nums[0]
        for i in range(1,ll-1): end[i] = max(nums[i],end[i-1])
        
        st  = [1 for _ in range(ll)]
        st[ll-1]=nums[ll-1]
        for i in range(1,ll-1):
            rev = ll-1-i
            st[rev] = min(nums[rev],st[rev+1])
        
        for i in range(1,ll-1):
            if nums[i-1] < nums[i] < nums[i+1]:
                if end[i-1]<nums[i] and nums[i]<st[i+1]:
                    b+=2
                else:
                    b+=1
        
        return b