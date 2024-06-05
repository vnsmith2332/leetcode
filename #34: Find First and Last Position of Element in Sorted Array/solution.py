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
                while curr_start > 0:
                    if nums[curr_start - 1] == target:
                        curr_start -= 1
                    else:
                        break
                while curr_end < len(nums) - 1:
                    if nums[curr_end + 1] == target:
                        curr_end += 1
                    else:
                        break
                return [curr_start, curr_end]

        return [-1, -1]
