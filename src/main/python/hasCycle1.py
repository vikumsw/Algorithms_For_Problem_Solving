# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head==None:
            return False
        
        fast = head
        slow = head
        
        while True:
            if fast.next == None or fast.next.next==None:
                return False
            else:
                if slow == fast.next or slow == fast.next.next:
                    return True
                else:
                    fast = fast.next.next
                    slow = slow.next