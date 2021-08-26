'''Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
'''

from collections import deque

class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.children = []

    def setChildren(self,children):
        self.children = children


def isConnected(s:Node,d:Node)->bool:
    if bfs(s,d) or  bfs(d,s): return True
    return False

def findDFS (s:Node,d:Node,found:list, vis:set)->None:
    if s in vis:
        return
    else:
        vis.add(s)
    
    if found[0]: return

    if d is s:
        found[0] = True
    else:
        for c in s.children:
            findDFS (c,d,found,vis)


def dfs_it(s,d)->bool:
    stack = [s]
    vis = set()

    while len(stack)>0:
        n = stack.pop()

        if n not in vis:
            vis.add(n)

            if n is d:
                return True
            else:
                for c in n.children:
                   stack.append(c)
    
    return False


def bfs(s,d)->bool:
    q = deque()
    q.append(s)
    vis = set()


    while len(q)>0:
        n = q.popleft()

        if n not in vis:
            vis.add(n)

            if n is d:
                return True
            else:
                for c in n.children:
                   q.append(c)
    
    return False







    return False


if __name__=="__main__":
    na = Node('A')
    nb = Node('B')
    nc = Node('C')
    nd = Node('D')
    ne = Node('E')
    nf = Node('F')

    na.setChildren([nc])
    nb.setChildren([])
    nc.setChildren([nb,nd])
    nd.setChildren([])
    ne.setChildren([nc])
    nf.setChildren([ne])


    print(isConnected(na,nf))