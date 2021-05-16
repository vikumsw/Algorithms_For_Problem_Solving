'''
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

1 <= nums.length <= 12
1 <= nums[i] <= 20
'''


class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        tot=0
        for i in range(1,len(nums)+1):
            c = combinations(nums,i)
            for i in c:
                temptot=0
                for k in i:
                    temptot = temptot ^ k

                tot += temptot
        return tot
        
