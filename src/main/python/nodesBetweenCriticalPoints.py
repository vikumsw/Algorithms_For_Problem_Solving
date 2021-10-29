# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        cp = []
        
        
        p = n = cur = None
        
        
        if head == None or head.next == None:
            return [-1,-1]
        
        p = head
        cur = head.next
        ind = 2
        while True:
            if cur.next == None:
                break
            
            if p.val<cur.val>cur.next.val:
                cp.append(ind)
                
            if p.val>cur.val<cur.next.val:
                cp.append(ind)
                
            p = cur
            cur = cur.next
            ind = ind + 1
            
        #print(cp)
        
        if len(cp)<2:
            return [-1,-1]
        
        ls = cp[0]
        mxd = cp[-1] - cp [0]
        cm = mxd
        for i in range(1,len(cp)):
            if cm > cp[i] - cp[i-1]:cm = cp[i] - cp[i-1]
                
        return [cm,mxd]