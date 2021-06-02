# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head

        newHead = self.reverseList(head.next)
        head.next = None
        head.next.next = head
        
        return newHead
