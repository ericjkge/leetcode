# Last updated: 7/14/2026, 10:20:57 PM
1class Solution:
2    def numDistinctIslands(self, grid: List[List[int]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        directions = [(1, 0, "d"), (0, 1, "r"), (-1, 0, "u"), (0, -1, "l")]
5        seen = set()
6
7        def dfs(r, c, path):
8            grid[r][c] = "#"
9            for dr, dc, s in directions:
10                nr, nc = r + dr, c + dc
11                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
12                    path.append(s)
13                    dfs(nr, nc, path)
14                    path.append("b")
15
16        count = 0
17        seen = set()
18        for r in range(rows):
19            for c in range(cols):
20                if grid[r][c] == 1:
21                    p = []
22                    dfs(r, c, p)
23                    if tuple(p) not in seen:
24                        seen.add(tuple(p))
25                        count += 1
26        
27        return count