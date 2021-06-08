class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:return [1]
        if rowIndex == 1:return [1,1]
        
        prev = [1,1]
        
        for i in range(2,rowIndex+1):
            print(i)
            r = []
            for j in range(0,i+1):
                if j==0 or j==i:r.append(1)
                else:r.append(prev[j-1]+prev[j])
            prev=r
        
        return prev
            
