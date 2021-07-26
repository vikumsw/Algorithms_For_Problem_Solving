class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        alph = "0abcdefghijklmnopqrstuvwxyz"
        
        def convert(s):
            l = list(map(lambda c:str(alph.index(c)),s))
            return "".join(l)
        
        def transformOnce(s):
            count = 0
            for c in s:
                count +=int(c)
            return str(count)
        
        def transformk(si,k):
            for i in range(k):
                si = transformOnce(si)
            return int(si)
        
        si = convert(s)
        #print(si)
        rv = transformk(si,k)
        
        
        return rv
