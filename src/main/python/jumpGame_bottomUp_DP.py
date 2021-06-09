class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False for _ in range(len(s))]
        dp[0] = True
        oneCount = 0
        for i in range(len(s)):
            if i > maxJump and dp[i - maxJump - 1]:oneCount -=1
            if i > minJump -1 and dp[i - minJump]:oneCount +=1
            if oneCount>0 and s[i] == '0' :dp[i]=True
        return dp[-1]
