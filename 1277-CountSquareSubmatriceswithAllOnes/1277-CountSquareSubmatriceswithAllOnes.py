# Last updated: 7/2/2026, 11:51:57 PM
1class Solution:
2    def countSquares(self, matrix: List[List[int]]) -> int:
3        m, n = len(matrix), len(matrix[0])
4
5        @cache
6        def dp(i, j):
7            if i >= m or j >= n or matrix[i][j] == 0:
8                return 0
9            
10            return 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))
11        
12        return sum(dp(i, j) for i in range(m) for j in range(n))
13