class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        sz = len(nums)
        ll = list(map(int,nums))
        ll.sort()
        
        return str(ll[sz-k])