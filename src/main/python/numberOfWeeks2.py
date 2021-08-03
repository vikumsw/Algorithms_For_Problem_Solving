class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:

        milestones.sort(reverse=True)
        weeks = 0
        lastIndex = -1
        while True:
            mx = 0
            mxIndex = -1

            #Traverse the milestones array find the mx and mxIndex
            for ind, value in enumerate(milestones):
                if value==0: continue
                elif mx<value and ind!=lastIndex:
                    mx = value
                    mxIndex = ind
                elif value<mx:break
                    
            if mx == 0:
                return weeks
            else:
                weeks +=1
                milestones[mxIndex] -=1
                lastIndex = mxIndex
        