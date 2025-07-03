# Last updated: 7/3/2025, 12:12:24 AM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        ans = []
        while left < right and top < bottom:
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1

            if len(ans) == len(matrix) * len(matrix[0]):
                break

            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        
        return ans