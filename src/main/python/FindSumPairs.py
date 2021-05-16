'''
you are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).
Implement the FindSumPairs class:

FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
'''

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
