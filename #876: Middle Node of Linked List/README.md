# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
On their first pass, most people think to find the length of the list, divide it by two, and use another loop to find the corresponding node. Is it possible to combine both of these steps into a single loop?


# Approach
<!-- Describe your approach to solving the problem. -->
We establish two pointers, `middle` and `fast`. `fast` moves through the linked list at the twice the speed of `middle`. Because `middle` is moving half as quickly, it will be in the middle of the linked list when `fast` reaches
the end.

# Complexity
- Time complexity: `O(n)`. We iterate over all values of the linked list.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`. No additional memory is required for larger lists.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            middle = middle.next
        return middle
```
