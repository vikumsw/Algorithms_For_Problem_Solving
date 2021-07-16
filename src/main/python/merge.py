class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        
        for i in range(n):
            nums1.pop()
            
        for n in nums2:
            while len(nums1) > p1 and nums1[p1]<n:
                p1 +=1
                
            nums1.insert(p1,n)
            p1 +=1
