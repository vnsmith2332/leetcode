# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Because the input array is sorted, binary search is the obvious solution for finding `target`. We are left to figure out how to adapt the binary search to identify a range of indices in which the value occurs.

# Approach
<!-- Describe your approach to solving the problem. -->
After finding that `target` is in the array, we can look to the left and right until we reach a different value. We return the two most recently visited indices in an array.

# Complexity
- Time complexity: The time complexity is `O(n)`. While the binary search is `log(n)`, the loop that identifies the range of indices will, in the worst case, require us to visit each value in the array.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`. No additional memory is required for larger inputs.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        high = len(nums) - 1
        low = 0
        
        while low <= high:
            mid = low + ((high - low) // 2)
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1

            else:
                curr_start = mid
                curr_end = mid

                # loop to identify the first occurrence
                while curr_start > 0:
                    if nums[curr_start - 1] == target:
                        curr_start -= 1
                    else:
                        break

                # loop to identify the last occurrence
                while curr_end < len(nums) - 1:
                    if nums[curr_end + 1] == target:
                        curr_end += 1
                    else:
                        break
                return [curr_start, curr_end]

        return [-1, -1]   
```
