# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
A palindrome is a sequence that is equivalent when read backwards. We need to inspect the elements of the linked list in reverse-order and compare these values to the original order to determine whether the elements
form a palindrome.

# Approach
<!-- Describe your approach to solving the problem. -->
We can utilize a stack to read the elements in reverse-order. We iterate over the list a single time to push all its values onto a stack. We then iterate over the list again, but this time we remove elements from the
stack at the same time. As we iterate from the front of the list, the elements on top of the stack are from the end of the list, making comparison easy.

If we are able to reach the end of the list and empty the stack without encountering unequal values, we return `True`.

# Complexity
- Time complexity: `O(n)`. 
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`. The stack requires all elements from the original list to be stored in memory.
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True     
```
