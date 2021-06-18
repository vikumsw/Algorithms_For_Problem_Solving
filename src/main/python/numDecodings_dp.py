class Solution:
    def numDecodings(self, s: str) -> int:
        
        def notValid():
            if len(s) == 0 :return True
            if s[0] == '0':return True
            for i in range(len(s)):
                if s[i] == '0' and s[i-1]!='1' and  s[i-1]!='2':
                    return True
            return False
        
        if notValid():return 0
        
        l = len(s)
        
        
        
        dp = [0 for _ in range(l) ]
        dp[0] = 1
        
        if l==1:return 1
        
        if s[1] == '0': dp[1] = 1
        elif int(s[:2])<27: dp[1] = 2
        else: dp[1] = 1
        
        if l==2:return dp[1]
        
        print(dp)
        for i in range(2,l):
            if s[i] == '0':
                dp[i] = dp[i-2]
            elif int(s[i-1]+s[i]) < 10:
                dp[i] = dp[i-1]
            elif int(s[i-1]+s[i]) < 27:
                dp[i] = dp[i-1]+ dp[i-2]
            else:
                dp[i] = dp[i-1]
       
        print(dp)
        return dp[l-1]
