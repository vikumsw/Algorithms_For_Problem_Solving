class Solution:
    cache = {}
    cache[1]=1
    cache[2]=2
    def climbStairs(self, n: int) -> int:
        if n in self.cache:return self.cache[n]
        count = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n]=count
        return count
        
