class Solution:
    def maxProduct(self, s: str) -> int:
        ll = len(s)

        def ternary(n):
            n = abs(n)
            if n < 3:
                return str(n)
            s = ''
            while n != 0:
                s = str(n%3) + s
                n = n//3
            return s
        
        def getStrings(s,selection):
            s1 = ''
            s2 = ''
            for i in range(len(s)):
                if selection[i] == '1':
                    s1 +=s[i]
                elif selection[i] == '2':
                    s2 +=s[i]
            return (s1,s2)
        
        def isPlalindrome(s):
            if s==s[::-1]:return True
            return False
        
        def isPlalindrome2(s):
            l = len(s)
            for i in range(l//2):
                if s[i]!=s[l-1-i]:
                    return False
            
            return True
        
        max_prod = 0
        sel_count = pow(3,ll)
        for i in range(sel_count):
            selection = ternary(i)
            selection = '0'*(len(s)-len(selection))+selection
            
            s1,s2 = getStrings(s,selection)
            if len(s1)==0:
                continue
                
            if len(s2)==0:
                continue
                
            if isPlalindrome2(s1) and isPlalindrome2(s2):
                prod = len(s1) * len(s2)
                max_prod = max(prod,max_prod)
                #print(selection,s1,s2,max_prod)
        
        return max_prod;
        
        
        
