# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
         
        def getPermutations(n):
            l = list()
            nums = [x for x in range(1,n+1)]            
            
            def genPerms(cur, rem ,permList):
                # base case
                if len(rem)==0:
                    permList.append(cur)
                    return
                
                for i in range(len(rem)):
                    r = list(rem)
                    r.pop(i)           
                    c = list(cur)
                    c.append(rem[i])           
                    genPerms(c, r ,permList)
                return
            
            permList = []                   
            genPerms([],nums,permList)
            return permList

                               
        bst_list = list()
        perm = getPermutations(n)
        
        
        def createBST(l):
            head = TreeNode(l.pop(0))
            
            def add(val,head):
                if head.val>val: 
                    if head.left == None: head.left = TreeNode(val)
                    else: add(val,head.left)
                else: 
                    if head.right == None: head.right = TreeNode(val)
                    else: add(val,head.right)
                
            for val in l:
                add(val,head)
            
            return head
        
        def isUnique(head,bst_list):
            def equal(t1,t2):
                if t1 == None and t2 == None:
                    return True
                if t1.val != t2.val:
                    return False
                
                return equal(t1.left,t2.left) and equal(t1.right,t2.right)
            
            for tree in bst_list:
                if equal(tree,head): return False
            
            return True
        
        for p in perm:
            bst = createBST(p)
            if isUnique(bst,bst_list): bst_list.append(bst)
        
        return bst_list
