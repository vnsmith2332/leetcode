# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Reversing a linked list requires us to point each node's `next` reference to the prior node.

# Approach
<!-- Describe your approach to solving the problem. -->
1. If there is no `head` or `head.next`, there is nothing to reverse, so immediately return `head`.
2. Start `curr` at the head of the list and `prev` at `None`
3. While the current node exists:
   * Save `curr.next` in a temporary variable so that the rest of the list is not lost when you reassign `curr`'s `next` reference
   * Set `curr.next` to point to the previous node
   * Set `prev` to `curr`
   * Set `curr` to be the old `curr.next`, which was saved in a temporary variable previously
4. Return `prev`, as this reference will now be at the "end" of the list, which is the new head.

# Complexity
- Time complexity: `O(n)`. 
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        prev = None
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        return prev
        
```
