class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        
        maxweeks = [0]
        
        def countWeeks(m,lastindex,count,maxweeks):
            
            #print('calling', m,lastindex,count,maxweeks)
            
            l = len(m)
            
            for i in range(l):
                if i != lastindex:
                    if m[i] == 0:
                        if count>maxweeks[0]:
                            maxweeks[0] = count
                    else:
                        temp  = m[:]
                        temp[i] = temp[i]-1
                        if count+1>maxweeks[0]:
                            maxweeks[0] = count+1
                        countWeeks(temp,i,count+1,maxweeks)
            
        countWeeks(milestones,-1,0,maxweeks)
        
        return maxweeks[0]