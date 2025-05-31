# Last updated: 5/31/2025, 3:27:06 PM
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        memo = {}
        def dp(row, col): # min cost to get to row, col
            if (row, col) in memo:
                return memo[(row, col)]
            
            if row == 0:
                return matrix[0][col]
            
            if col == 0: # left col
                memo[(row, col)] = min(dp(row - 1, 0), dp(row - 1, 1)) + matrix[row][col]
            elif col == n:
                memo[(row, col)] = min(dp(row - 1, n), dp(row - 1, n - 1)) + matrix[row][col]
            else:
                memo[(row, col)] = min(dp(row - 1, col - 1), dp(row - 1, col), dp(row - 1, col + 1)) + matrix[row][col]
                
            return memo[(row, col)]
        
        return min(dp(m, i) for i in range(n + 1))