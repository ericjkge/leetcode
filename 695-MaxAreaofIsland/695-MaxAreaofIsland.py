# Last updated: 2/3/2026, 10:18:07 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5        ans = 0
6
7        def dfs(r, c):
8            area = 1
9            grid[r][c] = -1
10            for dr, dc in directions:
11                nr, nc = r + dr, c + dc
12                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
13                    area += dfs(nr, nc)
14            return area
15
16        for r in range(rows):
17            for c in range(cols):
18                if grid[r][c] == 1: 
19                    ans = max(ans, dfs(r, c))
20        
21        return ans