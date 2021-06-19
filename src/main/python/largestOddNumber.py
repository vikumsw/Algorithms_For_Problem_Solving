class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        largest = ""
        
        l = len(num)
        for i in range(len(num)):
            if int(num[l-1-i])%2 == 1:
                largest = num[:l-i]
                break
        return largest