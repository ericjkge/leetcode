# Last updated: 8/14/2025, 11:21:47 PM
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.max = 0

        @cache
        def dp(i, j):
            if i == m or j == n or matrix[i][j] == "0":
                return 0

            right = dp(i, j + 1)
            down = dp(i + 1, j)
            diag = dp(i + 1, j + 1)

            side = 1 + min(right, down, diag)

            if side ** 2 > self.max:
                self.max = side ** 2

            return side
        
        for i in range(m):
            for j in range(n):
                dp(i, j)

        return self.max