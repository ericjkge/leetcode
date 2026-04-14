# Last updated: 4/14/2026, 10:40:17 AM
1class Solution:
2    def swimInWater(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5
6        def dfs(r, c, time):
7            if r == n - 1 and c == n - 1:
8                return True
9            
10            seen.add((r, c))
11            for dr, dc in directions:
12                nr, nc = r + dr, c + dc
13                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] <= time:
14                    if dfs(nr, nc, time):
15                        return True
16            return False
17
18        left, right = 0, n * n - 1
19        while left + 1 < right:
20            mid = (left + right) // 2
21            seen = set()
22            if grid[0][0] <= mid and dfs(0, 0, mid):
23                right = mid
24            else:
25                left = mid
26        
27        seen = set()
28        if grid[0][0] <= left and dfs(0, 0, left):
29            return left
30        return right