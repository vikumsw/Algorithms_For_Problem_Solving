# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        stack=[[root,0]]
        path_sum = 0
        
        if root==None:
            return False
        
        while stack:
            cur = stack.pop()
            path_sum = cur[1] + cur[0].val
            
            if cur[0].left:
                stack.append([cur[0].left,path_sum])
                
            if cur[0].right:
                stack.append([cur[0].right,path_sum])
            
            if cur[0].left==None and cur[0].right==None and path_sum == targetSum:
                return True
        
        return False
                
            
        