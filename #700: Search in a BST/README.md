# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
A binary search tree is easy to search, as values less than the current node are always found to the left, while values greater than the current node are always found to the right. We can use this to help us look for the value in the tree.

# Approach
<!-- Describe your approach to solving the problem. -->
Let's keep track of the node we are currently on with `current`. 
As long as `current` exists:
1. Check if `val` is less than `current.val`. If so, proceed to `current`'s left child.
2. Check if `val` is greater than `current.val`. If so, proceed to `current's` right child.
3. Otherwise, `current.val` is equal to `val`. This is the node we are looking for, so return it.

If we `current` is `None`, we've reached a leaf node without finding `val`. `val` does not exist in the tree, so we return `none`.

# Complexity
- Time complexity: `O(log(n))`, where `n` is the the number of nodes in the BST.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`. There is constant memory required to store `current`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        while current:
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                return current
        return None
```
