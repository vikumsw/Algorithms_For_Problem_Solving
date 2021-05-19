class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare2(a,b):
            if a==b:
                return 0
            elif str(a)+str(b) > str(b)+str(a):
                return 1
            else:
                return -1
        
        nums.sort(key= cmp_to_key(compare2) ,reverse=True)
        st = "".join(map(str,nums))
                     
        if st[0]=='0':
            return "0"
            
        return st
        
