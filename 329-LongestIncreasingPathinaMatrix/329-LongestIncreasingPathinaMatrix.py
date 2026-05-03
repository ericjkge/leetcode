# Last updated: 5/3/2026, 10:44:14 AM
1class Solution:
2    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
3        rows, cols = len(matrix), len(matrix[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5
6        @cache
7        def dp(r, c):
8            path = 1
9            for dr, dc in directions:
10                nr, nc = r + dr, c + dc
11                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
12                    path = max(path, 1 + dp(nr, nc))
13            return path
14        
15        longest = 0
16        for r in range(rows):
17            for c in range(cols):
18                longest = max(longest, dp(r, c))
19        return longest