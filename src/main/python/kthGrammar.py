class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n==1:
            return 0
        
        parent = self.kthGrammar(n-1,(k+1)//2)
        
        if k%2==0:
            res = 0 if parent==1 else 1
        else:
            res = parent
        
        return res
        
