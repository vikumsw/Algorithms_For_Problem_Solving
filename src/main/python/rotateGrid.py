class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        if len(grid)<1:
            return []
                
        def getInner(grid):
            inner = grid[1:-1]
            if len(inner) < 1:
                return []
            
            for i in range(len(inner)):inner[i] = inner[i][1:-1]
                
            if len(inner[0])<1:
                return []
            return inner
        
        def placeInner(grid,inner):
            
            if len(inner)<1: return
            
            for r in range(1,len(grid)-1):
                grid[r][1:-1] = inner[r-1]
                
            return grid
        
        def rotateOuter(grid,k):
            if len(grid)<1:
                return
            
            r,c = len(grid),len(grid[0])
            
            l = []
            for i in range(c): l.append(grid[0][i])
            for i in range(1,r-1): l.append(grid[i][c-1])
            for i in range(c): l.append(grid[r-1][c-1-i])
            for i in range(1,r-1): l.append(grid[r-1-i][0])
                
            n = k%len(l)
            
            for i in range(c): 
                grid[0][i] = l[n]
                n +=1
                n = n % len(l)
            for i in range(1,r-1):
                grid[i][c-1] = l[n]
                n +=1
                n = n % len(l)
            for i in range(c):
                grid[r-1][c-1-i] = l[n]
                n +=1
                n = n % len(l)
            for i in range(1,r-1):
                grid[r-1-i][0] = l[n]
                n +=1
                n = n % len(l)
        
        innerRotated = self.rotateGrid(getInner(grid),k)
        placeInner(grid,innerRotated)
        rotateOuter(grid,k)
        
        return grid
        
