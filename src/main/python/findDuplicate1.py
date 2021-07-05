class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem = [0 for i in range(100001) ]
        for n in nums:
            if mem[n]==1:
                return n
            else:
                mem[n] = 1