# Last updated: 1/15/2026, 11:53:49 AM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        time = 0
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5        rows, cols = len(grid), len(grid[0])
6        rotten = deque()
7        fresh = 0
8        time = 0
9
10        for r in range(rows):
11            for c in range(cols):
12                if grid[r][c] == 2:
13                    rotten.append((r, c))
14                if grid[r][c] == 1:
15                    fresh += 1
16        
17        if rotten:
18            time = -1
19
20        while rotten:
21            for _ in range(len(rotten)):
22                r, c = rotten.popleft()
23                for dr, dc in directions:
24                    nr, nc = r + dr, c + dc
25                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
26                        grid[nr][nc] = 2
27                        fresh -= 1
28                        rotten.append((nr, nc))
29            time += 1
30        
31        return time if fresh == 0 else -1