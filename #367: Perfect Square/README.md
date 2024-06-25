# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
A perfect square is a number that is the result of squaring an integer. We need to find some integer that, when squared, provides the input number.

# Brute Force Approach
<!-- Describe your approach to solving the problem. -->
The brute force approach requires us to iterate linearly over the range of numbers from 1 to the target number, `num` (inclusive). As we iterate, we square each number. If the result is equal to `num`, return `True`.
If we make it `num` without returning `True`, `num` is not a perfect square and we return `False`.

# Efficient Approach
The range of numbers from 1 to `num` is sorted data. This makes it suitable for a binary search. We start with the `low` pointer at 1 and the `high` pointer at `num`. Calculate `mid` as normal. If `mid` squared is greater than `num`, we search
only in the bottom half of the range. If `mid` squared is less than `num`, we only search in the higher half of the range. If `mid` squared is equal to `num`, we can return `True`.

# Complexity
- Time complexity: `O(log(n))`
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`. By not storing the range of numbers as we perform the binary search, we keep space complexity constant.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while high >= low:
            mid = low + (high - low) // 2
            if mid ** 2 > num:
                high = mid - 1
            elif mid ** 2 < num:
                low = mid + 1
            else:
                return True
        return False

```
