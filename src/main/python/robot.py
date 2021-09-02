
R = ["...x..","....xx","..x..."]


print("starting")

l = len(R)
m = len(R[0])

#0-right, 1-down, 2-left, 3-top
cur_dir = 0
cur_pos = (0,0)

vis = set()
vis.add((0,0))
visited = set()
visited.add((0,0,0)) #With direction

count = 1

def getNextPos(cur_pos,cur_dir):
    if cur_dir==0:
        return (cur_pos[0],cur_pos[1]+1)
    elif cur_dir==1:
        return (cur_pos[0]+1,cur_pos[1])
    elif cur_dir==2:
        return (cur_pos[0],cur_pos[1]-1)
    else:
        return (cur_pos[0]-1,cur_pos[1])


def isValid(nextPos,l,m):
    x = nextPos[0]
    y = nextPos[1]

    if x<0 or x>=l or y<0 or y>=m:
        return False
    
    return True

while True:
    nextPos = getNextPos(cur_pos,cur_dir)
    if isValid(nextPos,l,m) and R[nextPos[0]][nextPos[1]]==".":
        cur_pos = nextPos
        if (cur_pos[0],cur_pos[1],cur_dir) in visited:
            break

        if cur_pos not in vis:
            count +=1
            vis.add(cur_pos)
        
        visited.add((cur_pos[0],cur_pos[1],cur_dir))
    else:
        cur_dir = (cur_dir+1)%4

print(count)

