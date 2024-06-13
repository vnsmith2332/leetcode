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
