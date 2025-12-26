# Last updated: 12/26/2025, 11:22:29 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5
6        def dfs(r, c):
7            for dr, dc in directions:
8                nr, nc = r + dr, c + dc
9                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
10                    grid[nr][nc] = "-1"
11                    dfs(nr, nc)
12
13        counter = 0
14        for r in range(rows):
15            for c in range(cols):
16                if grid[r][c] == "1":
17                    counter += 1
18                    grid[r][c] = "-1"
19                    dfs(r, c)
20        
21        return counter