# Last updated: 3/29/2026, 9:02:50 PM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5
6        def dfs(r, c):
7            grid[r][c] = 0
8            area = 1
9            for dr, dc in directions:
10                nr, nc = r + dr, c + dc
11                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
12                    area += dfs(nr, nc)
13            return area
14        
15        ans = 0
16        for r in range(rows):
17            for c in range(cols):
18                if grid[r][c] == 1:
19                    ans = max(ans, dfs(r, c))
20        
21        return ans