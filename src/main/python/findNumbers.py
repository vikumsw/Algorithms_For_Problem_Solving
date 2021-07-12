class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        def isEven(n):
            if len(str(n))%2==0:return True
            
            return False
        
        def isEven1(n):
            dc=0
            while n>0:
                dc += 1
                n = n//10
            
            if dc%2==0:return True
            
            return False
        
        count = 0
        for n in nums:
            if isEven1(n): count +=1
                
        return count
