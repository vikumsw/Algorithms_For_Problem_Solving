class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        zero_max = 0
        one_max = 0
        zeros   = False
        ones    = False
        if s[0] == "0":
            zeros = True
        else:
            ones  = True
                
        count =0
        for c in s:
            if zeros and c=="0":
                count += 1
                zero_max = max(zero_max,count)
            elif ones and c=="1":
                count += 1
                one_max = max(one_max,count)
            else:
                count = 1
                if zeros:
                    zeros = False
                    ones  = True
                else:
                    zeros = True
                    ones  = False
            
        return one_max>zero_max
