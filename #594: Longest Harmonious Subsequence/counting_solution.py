class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        max_len = 0
        for num in num_count:
            if num + 1 in num_count:
                max_len = max(max_len, num_count[num] + num_count[num + 1])
        return max_len
