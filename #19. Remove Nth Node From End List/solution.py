# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        left = head
        right = head
        space = 0

        while space < n:
            space += 1
            right = right.next

        left_prev = None
        while right:
            right = right.next
            left_prev = left
            left = left.next
        if left_prev:
            left_prev.next = left.next
            return head
        return head.next
        
