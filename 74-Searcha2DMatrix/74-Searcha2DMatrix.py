# Last updated: 7/25/2025, 12:32:52 AM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left + 1 < right:
            mid = (left + right) // 2
            r, c = mid // cols, mid % cols
            if matrix[r][c] <= target:
                left = mid
            else:
                right = mid
        
        if matrix[left // cols][left % cols] == target:
            return True
        if matrix[right // cols][right % cols] == target:
            return True
        return False