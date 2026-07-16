# Last updated: 7/15/2026, 8:37:05 PM
1class Solution:
2    def maximalSquare(self, matrix: List[List[str]]) -> int:
3        rows, cols = len(matrix), len(matrix[0])
4
5        @cache
6        def dp(i, j):
7            if i >= rows or j >= cols or matrix[i][j] == "0":
8                return 0
9            
10            return 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))
11
12        return max(dp(r, c) for r in range(rows) for c in range(cols)) ** 2