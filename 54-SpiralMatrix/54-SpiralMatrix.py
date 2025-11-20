# Last updated: 11/20/2025, 12:04:19 PM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        ans = []

        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                ans.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])
            right -= 1

            if left > right or top > bottom:
                break

            for c in range(right, left - 1, -1):
                ans.append(matrix[bottom][c])
            bottom -= 1

            for r in range(bottom, top - 1, -1):
                ans.append(matrix[r][left])
            left += 1

        return ans