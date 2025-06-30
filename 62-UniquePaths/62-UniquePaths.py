# Last updated: 6/30/2025, 12:51:38 AM
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(i, j):
            if i == 0 or j == 0:
                return 1
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
            return memo[(i, j)]
        
        return dp(m - 1, n - 1)