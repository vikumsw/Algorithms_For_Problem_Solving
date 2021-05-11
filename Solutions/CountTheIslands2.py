from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #init the set
        visited = set ()
        
        count = 0
        for i,ii in enumerate(grid):
            for j,jj in enumerate(ii):
                pos = str(i)+" "+str(j)
                print(pos)
                if pos in visited:
                    continue
                
                if jj == '1':
                    count = count + 1
                    #add all island nodes to visited
                    #add node to queue
                    q = deque()
                    q.append(pos)
                    while q:
                        node = q.popleft()
                        x= int(node.split()[0])
                        y= int(node.split()[1])
                        print(x,y)
                        if len(grid)-1 >= x+1 and grid[x+1][y] == '1' and node not in visited:
                            q.append(str(x+1)+" "+str(y))
                        if len(grid[0])-1 >= y+1 and grid[x][y+1] == '1' and node not in visited:
                            q.append(str(x)+" "+str(y+1))
                        if 0 <= x-1 and grid[x-1][y] == '1' and node not in visited:
                            q.append(str(x-1)+" "+str(y))
                        if 0 <= y-1 and grid[x][y-1] == '1' and node not in visited:
                            q.append(str(x)+" "+str(y-1))
                            
                        visited.add(node)
                #add to set
                visited.add(pos)
        
        return count
