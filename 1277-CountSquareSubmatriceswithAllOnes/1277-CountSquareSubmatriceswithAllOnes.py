# Last updated: 8/14/2025, 11:37:36 PM
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        total = 0

        @cache
        def dp(i, j):
            if i == m or j == n or matrix[i][j] == 0:
                return 0
            
            right = dp(i, j + 1)
            down = dp(i + 1, j)
            diag = dp(i + 1, j + 1)

            return 1 + min(right, down, diag)

        for i in range(m):
            for j in range(n):
                total += dp(i, j)

        return total