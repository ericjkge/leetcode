# Last updated: 2/12/2026, 1:42:54 PM
1class Solution:
2    def swimInWater(self, grid: List[List[int]]) -> int:
3        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
4        n = len(grid)
5
6        def dfs(r, c, time):
7            if grid[r][c] > time:
8                return False
9
10            if (r, c) == (n - 1, n - 1):
11                return True
12            
13            seen.add((r, c))
14
15            for dr, dc in directions:
16                nr, nc = r + dr, c + dc
17                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] <= time:
18                    if dfs(nr, nc, time):
19                        return True
20            
21            return False
22        
23        left, right = 0, max(max(row) for row in grid)
24        while left + 1 < right:
25            seen = set()
26            mid = (left + right) // 2
27            if dfs(0, 0, mid):
28                right = mid
29            else:
30                left = mid
31        
32        seen = set()
33        if dfs(0, 0, left):
34            return left
35        return right