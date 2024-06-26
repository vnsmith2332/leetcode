# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
In thinking about this problem, we can identify some important facts about it:
1. Any harmonious subsequence will contain exactly two integers. It is not possible for a subsequence to contain more or less than two integers and the difference between its maximum
  and minimum values to equal 1.
2. The longest harmonious subsequence (LHS) will consist of the two digits in the array that have a difference of 1 and have the greatest number of combined occurrences, relative to
   the other digits in the array that form a harmonious subsequence.
3. When determining the LHS, the order of the digits in the input array does not matter. If all digits - except the two forming the harmonious subsequence -  were removed
   from the array, the harmonious subsequence would remain. The length of this subsequence does not change if the order of its elements changes.

# Sorting + Sliding Window Approach
My first thought in solving this problem was to find a way to apply a sliding window technique, since we are attempting to maximize some value
over a subset of the array. To use a sliding window, we take advantage of fact 3 above and sort the array. We then utilize a `left` and `right` pointer. We check if the
element at index `right` is harmonious with the element at index `left`. If it is, we increase the size of the window (increase `right` by one) to see if the sequence can be
any larger. We also get the size of the current sequence (`right` - `left` + 1) and check to see if it is the largest we've encountered.

If `nums[right] - nums[left]` is equal to `0`, we increase the size of the window, as the next element could form a harmonious subsequence.

If `nums[right] - nums[left]` is greater than `1`, we have passed the value with which `nums[left]` can form a harmonious subsequence. We shrink the window by increasing `left`.

Finally, return the length of the LHS.


### Complexity
- Time complexity: `O(n + nlog(n))`. Sorting the array is `O(nlog(n))`. We then iterate over the array a single time with the sliding window, which is `O(n)` complexity.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`. The memory requirements do not increase with the size of the input array.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Code
```python
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = 1
        max_len = 0
        curr_len = 0
        while right < len(nums):
            if nums[right] - nums[left] == 1:
                curr_len = right - left + 1
                right += 1
                if curr_len > max_len:
                    max_len = curr_len
            elif nums[right] - nums[left] == 0:
                right += 1
            else:
                left += 1
                curr_len = 0
        return max_len
```

# Counting Approach
<!-- Describe your approach to solving the problem. -->
we can use observation #2 from above to derive a second approach to this problem. We can count the occurrences of each digit in the array using a hash table.
Then, we iterate over the keys in the has table and, for each key, we check if `key + 1` is in the table. If it is, we find the length of harmonious subsequence they
form by summing the occurrences of the two digits. Save the greater of `max_length` and the length of the current harmonious subsequence.

### Complexity
- Time complexity: `O(n + m)` where `n` is the length of the input array and `m` is the number of *distinct* elements in the input array.
  The counting approach requires us to iterate over the input array a single time (`O(n)`) and then over a hash table of distinct elements (`O(m)`).
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`. The hash table requires size proportional to the size of the input array.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

### Code
```python
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        max_len = 0
        for num in num_count:
            if num + 1 in num_count:
                max_len = max(max_len, num_count[num] + num_count[num + 1])
        return max_len
```
