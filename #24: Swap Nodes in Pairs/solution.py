# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head.next)
        current = head
        prev = None
        while current and current.next:
            nex = current.next
            current.next = nex.next
            nex.next = current
            if prev:
                prev.next = nex
            prev = current
            current = current.next
        return dummy.next
      
