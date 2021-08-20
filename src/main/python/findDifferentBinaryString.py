class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        cache = set()
        for e in nums:
            cache.add(e)
                
        for i in range(2**n):
            bs = bin(i)[2:]
            if len(bs)<n:
                k = n-len(bs)
                bs = "0"*k + bs
            
            if bs in cache: continue
            
            return bs
        
        
        