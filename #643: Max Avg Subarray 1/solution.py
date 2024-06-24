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
        
