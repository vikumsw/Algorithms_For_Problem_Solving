class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        
        
        mat = [[-1 for _ in range(c)] for _ in range(r)]
        
        mat[0][0] = grid[0][0]
        for i in range(1,c): mat[0][i] = mat[0][i-1] + grid[0][i]
        for i in range(1,r): mat[i][0] = mat[i-1][0] + grid[i][0]
        
        for i in range(1,r):
            for j in range(1,c):
                mat[i][j] = min(mat[i-1][j],mat[i][j-1]) + grid[i][j]
            
        return mat[r-1][c-1]