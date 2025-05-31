# Last updated: 5/31/2025, 3:27:24 PM
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp[0][0] = 1
        
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
        
        for i in range (1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
            
        
        
#         @cache
#         def dfs(row, col):
#             if row + col == 0 and obstacleGrid[row][col] == 0:
#                 return 1
            
#             paths = 0
#             if row > 0 and obstacleGrid[row][col] == 0:
#                 paths += dfs(row - 1, col)
#             if col > 0 and obstacleGrid[row][col] == 0:
#                 paths += dfs(row, col - 1)
                
#             return paths
            
#         m = len(obstacleGrid) - 1
#         n = len(obstacleGrid[0]) - 1
#         return dfs(m, n)