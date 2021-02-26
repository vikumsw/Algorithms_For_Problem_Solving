'''
Zigzag Traversal
"Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right, then right to left for the next level, alternating in the same way for all levels."
'''

class Node:
    def __init__(self, val,left,right):
        self.val = val
        self.left = left
        self.right = right

def zigZagTraversal(head:Node)->list:
    zz_l = []
    RTL = False
    queue = [head]
    while queue:
        if RTL:
            for i in range(len(queue)):
                zz_l.append(queue[len(queue)-1-i].val)
        else:
            for i in range(len(queue)):
                zz_l.append(queue[i].val)
        
        temp = []
        for e in queue:
            if e.left:
                temp.append(e.left)
            if e.right:
                temp.append(e.right) 
        
        queue = temp

        if RTL:RTL=False
        else: RTL=True

    return zz_l

if __name__ == "__main__":

    head = Node(1,None,None)
    head.left , head.right = Node(2,None,None), Node(3,None,None)
    head.left.left, head.left.right , head.right.left, head.right.right = Node(4,None,None), Node(5,None,None),Node(6,None,None), Node(7,None,None)
    head.left.left.left, head.left.left.right = Node(8,None,None), Node(9,None,None)
    print(zigZagTraversal(head))



