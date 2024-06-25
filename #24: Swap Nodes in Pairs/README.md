# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->
### Handling Edge Cases
First, check that `head` and `head.next` exist. If either are missing, there are no pairs to swap. Return `head` immediately.

### Handling Head Reassignment
We know `head.next` exists, and we know that this will be the new head of our final list. To simplify things, we can create a dummy node that points to `head.next`. At the end, we return `dummy.next` to get the actual list.

### Performing Swaps
Proceed with the following algorithm to perform each swap:
* Keep track of the nodes `current` and `prev`; initialize these to `head` and `None`, repsectively.
* While `current` and `current.next` exist:
  * Assign `nex` to be `current.next`
  * Reassign `current`'s `next` reference to `nex.next`.
  * Reassign `nex`'s `next` reference to `current`. This step, along with the previous, perform the swap
  * `prev.next` still points to `current`, which is further along in the list. If `prev.next` is not `None`:
    * Reassign `prev`'s `next` reference to `nex`
  * Set `prev = current` and `current = current.next` to move to the next pair of nodes

# Complexity
- Time complexity: `O(n)`. This approach requires us to iterate over the entire list a single time.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`. Space requirements do not grow with input size.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
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

        
```
