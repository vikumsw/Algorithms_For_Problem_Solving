class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow2(x,n):
            if n==0:return 1
            res = pow2(x,int(n/2))**2
            if n%2==1: res*=x
            return res
        
        if n<0:return pow2(1/x,-n)
        else:return pow2(x,n)