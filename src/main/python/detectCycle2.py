# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None: return None
        
        cycleNode = None
        fast = head
        slow = head
        
        while True:
            if fast.next == None or fast.next.next == None:
                return None

            if slow == fast.next or slow == fast.next.next :
                cycleNode = slow
                break
            else:
                fast = fast.next.next
                slow = slow.next
        
        p2 = head
        
        while p2 != None:
            p1 = cycleNode
            while True:
                p1=p1.next
                if p1 == p2:
                    return p1
                if p1 == cycleNode:
                    break
            p2=p2.next
            
        return None