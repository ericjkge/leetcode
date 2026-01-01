# Last updated: 1/1/2026, 9:54:37 AM
1class Solution:
2    def swimInWater(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5
6        def dfs(r, c, time):
7            if r == n - 1 and c == n - 1:
8                return True
9            seen.add((r, c))
10
11            for dr, dc in directions:
12                nr, nc = r + dr, c + dc
13                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= time and (nr, nc) not in seen:
14                    if dfs(nr, nc, time):
15                        return True
16            return False
17
18        left, right = 0, n * n - 1
19
20        while left + 1 < right:
21            seen = set()
22            mid = (left + right) // 2
23            if grid[0][0] <= mid and dfs(0, 0, mid):
24                right = mid
25            else:
26                left = mid
27        
28        if grid[0][0] <= left and dfs(0, 0, left):
29            return left
30        return right