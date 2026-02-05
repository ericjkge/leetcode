# Last updated: 2/5/2026, 9:10:18 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5        counter = 0
6        
7        def dfs(r, c):
8            grid[r][c] = "-1"
9            for dr, dc in directions:
10                nr, nc = r + dr, c + dc
11                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
12                    dfs(nr, nc)
13        
14        for r in range(rows):
15            for c in range(cols):
16                if grid[r][c] == "1":
17                    counter += 1
18                    dfs(r, c)
19        
20        return counter
21                