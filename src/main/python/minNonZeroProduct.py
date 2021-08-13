class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        if p==1:
            return 1
        if p==2:
            return 6
        
        a = pow(2,p)-1
        b = pow(2,p)-2
        
        ans  = (pow(pow(2,p,10**9+7)-2,((a-3)/2),10**9+7)*a*b) %(10**9+7)
        
        return ans