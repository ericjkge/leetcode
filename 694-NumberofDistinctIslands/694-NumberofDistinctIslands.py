# Last updated: 7/14/2026, 10:29:43 PM
1class Solution:
2    def numDistinctIslands(self, grid: List[List[int]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        directions = [(1, 0, "d"), (0, 1, "r"), (-1, 0, "u"), (0, -1, "l")]
5        seen = set()
6
7        def dfs(r, c, cells):
8            grid[r][c] = "#"
9            for dr, dc, s in directions:
10                nr, nc = r + dr, c + dc
11                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
12                    cells.append((nr, nc))
13                    dfs(nr, nc, cells)
14
15        count = 0
16        seen = set()
17        for r in range(rows):
18            for c in range(cols):
19                if grid[r][c] == 1:
20                    cells = []
21                    dfs(r, c, cells)
22                    diff = tuple((row - r, col - c) for row, col in cells)
23                    if diff not in seen:
24                        seen.add(diff)
25                        count += 1
26        
27        return count