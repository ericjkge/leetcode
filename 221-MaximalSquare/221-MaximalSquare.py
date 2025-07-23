# Last updated: 7/23/2025, 11:50:58 PM
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        memo = {}

        @cache
        def dp(i, j): # Side length of max square with top left at (i, j)
            if i > rows or j > cols:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = 0
            down = dp(i + 1, j)
            right = dp(i, j + 1)
            diag = dp(i + 1, j + 1)

            if matrix[i][j] == "1":
                memo[(i, j)] = 1 + min(down, right, diag)
            
            return memo[(i, j)]
        
        dp(0, 0)
        return max(memo.values()) ** 2