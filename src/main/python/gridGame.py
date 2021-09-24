class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        for c in range(1,n):
            grid[0][c] = grid[0][c] + grid[0][c-1]
            grid[1][c] = grid[1][c] + grid[1][c-1]
        
        def calc(i,j):
            if i==j:return 0
            
            if j==0:
                return grid[1][i-1]
            
            if j==n-1:
                return grid[0][n-1] - grid[0][i]
            
        cur_min = 100000000000
        for i in range(n):
            mx = max(calc(i,0),calc(i,n-1))
            cur_min = min(mx,cur_min)
        
        
        return cur_min
        