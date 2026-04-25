# Last updated: 4/25/2026, 1:15:29 PM
1class Solution:
2    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
3        rows, cols = len(matrix), len(matrix[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5        
6        @cache
7        def dp(r, c):
8            longest = 1
9            for dr, dc in directions:
10                nr, nc = r + dr, c + dc
11                if 0 <= nr < rows and 0 <= nc < cols and matrix[r][c] < matrix[nr][nc]:
12                    longest = max(longest, 1 + dp(nr, nc))
13            
14            return longest
15        
16        ans = 0
17        for r in range(rows):
18            for c in range(cols):
19                ans = max(ans, dp(r, c))
20        
21        return ans
22