# Last updated: 11/22/2025, 3:22:13 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left + 1 < right:
            mid = (left + right) // 2
            r, c = mid // cols, mid % cols
            if matrix[r][c] < target:
                left = mid
            else:
                right = mid
        
        return matrix[left // cols][left % cols] == target or matrix[right // cols][right % cols] == target
