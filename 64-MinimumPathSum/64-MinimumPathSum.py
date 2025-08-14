# Last updated: 8/14/2025, 10:55:38 PM
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dp(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            
            if i == 0:
                return grid[0][j] + dp(0, j - 1)

            if j == 0:
                return grid[i][0] + dp(i - 1, 0)         

            return grid[i][j] + min(dp(i - 1, j), dp(i, j - 1))
        
        return dp(m - 1, n - 1)