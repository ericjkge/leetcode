# Last updated: 4/1/2026, 10:55:21 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5
6        def dfs(r, c):
7            grid[r][c] = "0"
8            for dr, dc in directions:
9                nr, nc = r + dr, c + dc
10                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
11                    dfs(nr, nc)
12        
13        count = 0
14        for r in range(rows):
15            for c in range(cols):
16                if grid[r][c] == "1":
17                    count += 1
18                    dfs(r, c)
19        
20        return count