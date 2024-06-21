# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
For most searching problems, we use either linear search for binary search. The matrix we are dealing with is sorted on two levels: the nested arrays are sorted (the first integer of each array is greater than the last integer of the previous array), and the values within each array are sorted. Sorted data allows us to use the binary search. We can use binary search first to identify which array to look in, then again to search that array for the target.

# Approach
<!-- Describe your approach to solving the problem. -->
## Finding the Array
Just like the usual binary search, we start with two pointers, `low` and `high` that are intialized to the beginning and end indices of the matrix, repsectively. While `low` is less than or equal to `high`:
1. Calculate `mid`, the middle array of the current search space.
2. Check if the `target` is less than *the first value of the middle array*. If it is, we immediately check if `target` is greater than the *the first value of the previous array* (that is, the array at index `mid - 1`. If this is true, we have found the array that target must be in, so we can end the binary search. Otherwise, set `high = mid - 1`.
3. Check if `target` is greater than *the first value of the middle array*. If it is, set `low = mid + 1`.
4. If `target` is equal to the first value of the middle array, immediately return `True`.

At first glance, this approach seems to pass up the correct array when `target` is found to be greater than `mid[0]`, as `target` could be in this array. However, the modification to the binary search (explained in step 2 above) accounts for this possibility.

## Finding the Target
Once the array that would contain `target` is identified, perform a standard binary search on that array. If `target` is found, return `True`. Otherwise, return `False`.


# Complexity
- Time complexity: `O(log(n * m))`, where `n` is the number of rows (the number of arrays in the matrix) and `m` is the number of columns (the length of each array in the matrix).
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        high = len(matrix) - 1
        low = 0
        while low <= high:
            mid_arr = low + (high - low) // 2
            if target < matrix[mid_arr][0]:
                if target > matrix[mid_arr - 1][0]:
                    mid_arr -= 1
                    break
                high = mid_arr - 1
            elif target > matrix[mid_arr][0]:
                low = mid_arr + 1
            else:
                return True
        
        high = len(matrix[mid_arr]) - 1
        low = 0
        while low <= high:
            mid = low + (high - low) // 2
            if target < matrix[mid_arr][mid]:
                high = mid - 1
            elif target > matrix[mid_arr][mid]:
                low = mid + 1
            else:
                return True
        return False
```
