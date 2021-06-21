class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        rc = len(grid2)
        cc = len(grid2[0])
        
        
        visited = set()
        
        def traverseIsland(r,c,ll):
            if r<0 or r>rc-1 or c<0 or c>cc-1:
                return
            
            if (r,c) in visited:
                return
            
            if grid2[r][c] == 0:
                visited.add((r,c))
                return
            else:
                if grid1[r][c] == 1:
                    ll.append(1)
                else:
                    ll.append(0)
                visited.add((r,c))
                traverseIsland(r-1,c,ll)
                traverseIsland(r+1,c,ll)
                traverseIsland(r,c-1,ll)
                traverseIsland(r,c+1,ll)
                
            
        for r in range(rc):
            for c in range(cc):
                print(grid1[r][c], end=" ")
            print()
        
        print()
        
        for r in range(rc):
            for c in range(cc):
                print(grid2[r][c], end=" ")
            print()
        
        sub = 0
        for r in range(rc):
            for c in range(cc):
                
                if (r,c) not in visited: 
                    print(grid2[r][c], end=" ")
                
                if (r,c) not in visited and grid2[r][c] == 1:
                    ll = list()
                    traverseIsland(r,c,ll)
                    if all(ll):
                        sub +=1 
            
        return sub