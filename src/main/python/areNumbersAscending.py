class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        ss=set()
        for i in range(1,100):
            ss.add(str(i))
        
        #print(ss)
        l = s.split()
        #print(l)
        
        last = 0
        for w in l:
            if w in ss:
                if int(w)>last:
                    last = int(w)
                else:
                    return False
        
        return True