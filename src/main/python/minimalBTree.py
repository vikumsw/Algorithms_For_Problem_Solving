'''
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
'''

class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
    
    def add(self,val):
        pass



def createBtree(arr,s,e):
    if s>e: return
    mid = (s+e)//2
    add(arr[mid])
    createBtree(arr,s,mid-1)
    createBtree(arr,mid+1,e)

createBtree([1,2,3,4,5,6,7,8,9])