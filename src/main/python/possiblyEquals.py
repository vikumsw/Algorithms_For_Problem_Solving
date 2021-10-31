class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        
        # i18n
        # [i.........n,i..................n]
        
        def getTemplates(s):
            ll = [""]
            
            num = ''
            for i,e in enumerate(s):
                if ord('a')<=ord(e)<=ord('z') or i==len(s)-1:
                    if ord('0')<=ord(e)<=ord('9'):
                        num = num + e
                    #print(num)
                    if len(num) == 1:
                        for i in range(len(ll)):
                            ll[i]=ll[i] +"."*int(num)
                    if len(num) == 2:
                        l1 = ll[:]
                        for i in range(len(ll)):
                            ll[i]=ll[i] +"."*(int(num[0])+int(num[1]))
                            l1[i]=l1[i] +"."*int(num)
                        
                        ll = ll + l1
                    if len(num) == 3:
                        l1 = ll[:]
                        l2 = ll[:]
                        l3 = ll[:]
                        
                        for i in range(len(ll)):
                            ll[i]=ll[i] +"."*(int(num[0])+int(num[1])+int(num[2]))
                            l1[i]=l1[i] +"."*(int(num[:2])+int(num[2]))
                            l2[i]=l2[i] +"."*(int(num[:1])+int(num[1:]))
                            l3[i]=l3[i] +"."*(int(num))

                        ll = ll + l1 + l2 + l3
                    
                    num = ''
                
                
                
                if ord('a')<=ord(e)<=ord('z'):
                    for i in range(len(ll)):
                        ll[i]=ll[i]+e
                
                if ord('0')<=ord(e)<=ord('9'):
                    num = num + e
                    
                
                        
            return ll
                        
        #print(getTemplates("i123n"))
        #print(getTemplates("i18"))
        
        def match(s1,s2):
            l = len(s1)
            if l != len(s2):
                return False
            
            for i in range(l):
                if s1[i] == '.' or s2[i] == '.':
                    continue
                elif s1[i] != s2[i]:
                    return False
            
            return True
                
        #print(match("....","aabb"))
        #print(match("a..b","aabb"))
        #print(match("b..b","aabb"))
        
        l1 = getTemplates(s1)
        l2 = getTemplates(s2)
        
        for t1 in l1:
            for t2 in l2:
                if match(t1,t2):
                    return True
                
        return False  
            