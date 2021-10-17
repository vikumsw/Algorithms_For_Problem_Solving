class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def isBalanced(n):
            s = str(n)
            m = DefaultDict(int)
            for c in s:
                m[c] = m[c]+1
                
            for e in m:
                if not m[e]==int(e): return False
                
            return True
            
        
        
        while True:
            n = n+1
            if isBalanced(n): return n
        