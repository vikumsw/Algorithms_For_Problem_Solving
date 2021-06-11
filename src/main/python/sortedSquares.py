class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def isValid(n):
            return -1<n<l
        
        l = len(nums)
        p1 , p2 = 0,0
        
        for i in range(l):
            if nums[i]>=0:
                p2 = i
                p1 = p2-1
                break
                
            p2 = i+1
            p1 = i
                
        ll = []
        
        while(p1>-1 or p2<l):
            if -1<p1<l and -1<p2<l:
                if -nums[p1]>=nums[p2]:
                    ll.append(nums[p2]**2)
                    p2 += 1
                else:
                    ll.append(nums[p1]**2)
                    p1 -= 1
            elif -1<p1<l:
                ll.append(nums[p1]**2)
                p1 -= 1
            else:
                ll.append(nums[p2]**2)
                p2 += 1
        
        return ll