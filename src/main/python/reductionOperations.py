class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        d = defaultdict(int)
        for e in nums:
            d[e]=d[e]+1
            
        s =len(d)
        i = 0
        count = 0
        for e in d.keys():
            count += i*d[e]
            i=i+1
            
        return count