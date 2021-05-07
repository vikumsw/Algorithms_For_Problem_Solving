class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:        
        people.sort(key=lambda item: (item[1], -item[0]))
        
        finalList = []
        
        for itm in people:
            val = itm[0]
            expected_count = itm[1]
            if expected_count==0:
                finalList.insert(0,itm)
                continue
                
            l = len(finalList)
            count= 0
            ind  = 0
            for i in range(l):
                if finalList[i][0]>=val:
                    count += 1
                    if count == expected_count:
                        ind = i+1
                        break
            finalList.insert(ind,itm)
        
        return finalList