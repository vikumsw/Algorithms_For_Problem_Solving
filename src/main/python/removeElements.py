# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        cur = head
        prev = None
        while cur != None:
            if cur.val == val:
                if prev == None:
                    head = cur.next
                else:   
                    prev.next = cur.next
            else:
                prev = cur
                
            cur = cur.next
            
        return head
