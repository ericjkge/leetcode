# Last updated: 2/24/2026, 8:43:08 AM
1class Solution:
2    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
3        rows, cols = len(matrix), len(matrix[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5
6        @cache
7        def dp(r, c):
8            path = 0
9            for dr, dc in directions:
10                nr, nc = r + dr, c + dc
11                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
12                    path = max(path, dp(nr, nc))
13            return path + 1
14
15        longest = 0
16        for r in range(rows):
17            for c in range(cols):
18                longest = max(longest, dp(r, c))
19        return longest