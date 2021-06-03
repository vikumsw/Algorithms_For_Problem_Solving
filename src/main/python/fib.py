class Solution:
    cache = {}
    def fib(self, n: int) -> int:
        
        if n<2: return n
        
        if n in self.cache: return self.cache[n]
        
        result = self.fib(n-1) + self.fib(n-2)
        self.cache[n] = result
        
        return result
