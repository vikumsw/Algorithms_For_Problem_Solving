class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:return [1]
        if rowIndex == 1:return [1,1]
        
        prev = self.getRow(rowIndex-1)
        l = [prev[i-1] + prev[i] for i in range(1,rowIndex)]
        l.insert(0,1)
        l.append(1)
        return l
