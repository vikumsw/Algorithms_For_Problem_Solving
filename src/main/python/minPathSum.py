class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = {}
        r = len(grid)
        c = len(grid[0])
        
        def sum(r,c):
            if r<0 or c<0:
                return 100000000
            if (r,c) == (0,0):
                return grid[0][0]
            
            if (r,c) in cache:
                return cache[(r,c)]
            
            sum1 = min(sum(r-1,c),sum(r,c-1)) + grid[r][c]
            cache[(r,c)] = sum1
            return sum1
        
        return sum(r-1,c-1)