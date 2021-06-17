class Solution:
    cache = {}
    def numDecodings(self, s: str) -> int:
        
        def notValid():
            if s[0] == '0':return True
            for i in range(len(s)):
                if s[i] == '0' and s[i-1]!='1' and  s[i-1]!='2':
                    return True
            return False
        
        if len(s) > 0 and notValid(): return 0
        
        if len(s) == 0: return 0
        elif len(s) == 1:return 1
        elif len(s) == 2:
            num = int(s)
            if num == 10 or num ==20 : return 1
            elif num<27: return 2
            else: return 1
        
        
        if s in self.cache:return self.cache[s]
        
        last2 = int(s[-2:])
        last  = int(s[-1:])
        
        count = 0
        if last == 0:
            if last2==10 or last2==20 :
                count = self.numDecodings( s[:-2])
            else:
                return 0
        else:
            if 10<last2<27:
                count = self.numDecodings( s[:-1]) + self.numDecodings( s[:-2])
            else:
                count = self.numDecodings( s[:-1])
                
        self.cache[s] = count
        
        return count
