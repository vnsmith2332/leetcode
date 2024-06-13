# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The difficult part of this problem is identifying which node is the `n`th node from the end in a single pass. A single pointer would allow us to identify the correct node in two iterations: one to find the length of the list, and one more
to find the `n`th node from the end and remove it. By using a second pointer, we can measure the space that should exist between the two pointers when one is at the end and the other is `n` nodes away from the end.

# Approach
<!-- Describe your approach to solving the problem. -->
We can apply our intuition to use two pointers using the following algorithm:
1. Initialize two pointers, `right` and `left`, at the `head` of the list. Initialize one more pointer, `left_prev` as `None`.
2. Move `right` to the next node until `right` is `n` nodes ahead of `left`
3. While `right` is not at the end of the list, move both `right` and `left` to the next node. `left_prev` becomes `left` on each iteration.
4. Once `right` reaches the end, `left` will point to the node that needs to be removed. Point `left_prev.next` to `left.next` and return `head`.

This approach works because when `right` is at the end, `left` is `n` nodes behind (and `n` nodes from the end of the list) due to the head start `right` received at the beginning of the algorithm.

# Complexity
- Time complexity: `O(n)`. The algorithm requires us to iterate over every node in the list.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`. The algorithm requires constant space for three pointers (`right`, `left`, and `left_prev`) regardless of the size of the linked list.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
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
        

```
