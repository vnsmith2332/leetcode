# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem requires us to maximize some value within a subsection of an iterable. These characteristics indicate a sliding window technique is required.

# Approach
<!-- Describe your approach to solving the problem. -->
We define the window to be `nums[left : right]`. `left` begins at `0` and `right` begins at `k`. We divide the sum of this window by `k` to get the intial `max_avg`. We proceed with the sliding window, subtracting the value one
index behind the window, while adding the value one index ahead of the window and finding the average. If the average exceeds `max_avg`, replace `max_avg`. Inrease `left` and `right` by one each time.

Subtracting and adding the values preceeding and following the window (respectively) greatly increases the efficiency of the algorithm, as we do not have to look at all the elements in the window again to obtain the sum.

# Complexity
- Time complexity: `O(n)`. Our window passes over the entire array once.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`. Space requirements do not increase with larger inputs.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[0:k])
        max_avg = window_sum / k
        left = 1
        right = k
        while right < len(nums):
            window_sum = window_sum - nums[left-1] + nums[right]
            curr_avg = window_sum / k
            if curr_avg > max_avg:
                max_avg = curr_avg
            left += 1
            right += 1
        return max_avg
        
```
