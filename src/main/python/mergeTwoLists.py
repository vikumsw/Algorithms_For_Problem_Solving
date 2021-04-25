# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return  l2
        elif not l2: return l1
        
        if l1.val>l2.val:
            l2.next = self.mergeTwoLists(l1,l2.next)
            head = l2
        else:
            l1.next = self.mergeTwoLists(l1.next,l2)
            head = l1
        
        return head
        