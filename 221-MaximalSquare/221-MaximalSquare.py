# Last updated: 7/2/2026, 11:32:54 PM
1class Solution:
2    def maximalSquare(self, matrix: List[List[str]]) -> int:
3        m, n = len(matrix), len(matrix[0])
4        @cache
5        def dp(i, j):
6            if i >= m or j >= n or matrix[i][j] == "0":
7                return 0
8
9            return 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))
10        
11        return max(dp(i, j) for i in range(m) for j in range(n)) ** 2
12