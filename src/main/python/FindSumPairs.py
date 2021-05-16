class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.dict2 = {}
            
        for n in self.nums2:
            self.dict2[n] = self.dict2.get(n,0)+1
        

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.dict2[self.nums2[index]] = self.dict2.get(self.nums2[index]) - 1
        self.dict2[self.nums2[index] + val] = self.dict2.get(self.nums2[index] + val,0) + 1
        self.nums2[index] +=val
        
        
        

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        count = 0
        for i in self.nums1:
            count += self.dict2.get(tot-i,0)

        
        return count
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
