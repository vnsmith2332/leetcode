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
