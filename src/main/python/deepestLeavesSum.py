# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        sums = defaultdict(int)
        
        q = deque()
        q.append([root,0])
        
        while q:
            cur = q.popleft()
            if cur[0].left==None and cur[0].right==None:
                sums[cur[1]]+=cur[0].val
            
            if cur[0].left:
                q.append([cur[0].left,cur[1]+1])
            
            if cur[0].right:
                q.append([cur[0].right,cur[1]+1])
                
        #print(sums)
        return sums[max(sums.keys())]
        