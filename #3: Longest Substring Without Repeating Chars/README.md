# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem asks us to find some subset of an iterable that maximizes some condition. These characteristics point to a solution involving a sliding window.

# Approach
<!-- Describe your approach to solving the problem. -->
We start with two pointers, `left` and `right` that define the boundaries of our window. Additionally, we utilize a set, `seen`, to keep track of characters that are in the window we are currently looking at (i.e., between the indices `left` and `right`). `max_len`
tracks the longest substring we've seen so far. The algorithm proceeds as follows:
1. While `right` is less than the length of the input string, `s`:
    * If `s[right]` is not in `seen`, we've encountered a character unique to the substring. Add it to `seen` and check if `seen.length` is now greater than `max_len`. If so, update `max_len`.
    * If `s[right]` is in `seen`, our window contains a duplicate character, so we need to shrink the window. We do this by moving the `left` pointer to the right while simultaneously removing the characters from `seen` that `left` encounters. Continue doing this until
      the duplicate character has been removed from `seen`. Finally, add `s[right]` to `seen`. This approach ensures that our window starts and ends in positions that can maximize the length of subsequent substrings.
    * Increase `right` by one to examine the next character in `s`.
2. After `right` has iterated over all characters in `s`, return `max_len`. 

# Complexity
- Time complexity: `O(n)`. This sliding window technique provides linear time complexity by allowing a single pass over `s`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        max_len = 0
        while right < len(s):
            # char at right of window is not in the substring. Add it and check for max length
            if s[right] not in seen:
                seen.add(s[right])
                if len(seen) > max_len:
                    max_len = len(seen)
            # char at right of window is in the substring. Shrink window until this char is removed, then add it back in
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
            right += 1
        return max_len      
```
