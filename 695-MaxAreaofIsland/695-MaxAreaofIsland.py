# Last updated: 2/3/2026, 10:15:32 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5        self.max = 0
6
7        def dfs(r, c):
8            grid[r][c] = -1
9            for dr, dc in directions:
10                nr, nc = r + dr, c + dc
11                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
12                    self.area += 1
13                    dfs(nr, nc)
14
15
16        for r in range(rows):
17            for c in range(cols):
18                self.area = 0
19                if grid[r][c] == 1: 
20                    self.area += 1
21                    dfs(r, c)
22                self.max = max(self.max, self.area)
23        
24        return self.max