class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        def flarge(s,f):
            if int(s[:2])>int(f[:2]): return False
            elif int(s[:2])<int(f[:2]):return True
            else:
                if int(s[3:]) < int(f[3:]):
                    return True
        
        def getStartNum(s):
            h = int(s[:2])
            m = int(s[3:])
            
            r = 0
            if m==0:r = 0
            elif m<16:r = 15
            elif m<31:r = 30
            elif m<46:r = 45
            else : r = 60
                
            return 4*h + r//15
        
        def getFinishNum(f):
            h = int(f[:2])
            m = int(f[3:])
            
            r = 0
            if m<15:r = 0
            elif m<30:r = 1
            elif m<45:r = 2
            else:r = 3
                
            return 4*h + r 
        
        s=getStartNum(startTime)
        f=getFinishNum(finishTime)
        
        print(s,f)
        rounds = 0
        if flarge(startTime,finishTime):
            rounds = f - s
        else:
            rounds = (96 - s) + f
        
        return rounds if rounds>-1 else 0