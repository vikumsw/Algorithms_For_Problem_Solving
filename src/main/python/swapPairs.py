# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(h):
            if not h:
                return None
            if not h.next:
                return h
            
            first = h
            second = h.next
            third = swap(h.next.next)
            
            first.next  = third
            second.next = first
            return second
        
        return swap(head)