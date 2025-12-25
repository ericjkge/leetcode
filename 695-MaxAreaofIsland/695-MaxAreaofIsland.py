# Last updated: 12/25/2025, 8:30:02 PM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        ans = 0
5        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
6
7        def dfs(r, c):
8            area = 1
9            for dr, dc in directions:
10                nr, nc = r + dr, c + dc
11                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
12                    grid[nr][nc] = -1
13                    area += dfs(nr, nc)
14            return area
15        
16        for r in range(rows):
17            for c in range(cols):
18                if grid[r][c] == 1:
19                    grid[r][c] = -1
20                    area = dfs(r, c)
21                    ans = max(ans, area)
22        
23        return ans