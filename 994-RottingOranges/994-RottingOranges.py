# Last updated: 2/27/2026, 8:56:21 AM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        rotten = deque()
5        time = 0
6        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
7        fresh = 0
8
9        for r in range(rows):
10            for c in range(cols):
11                if grid[r][c] == 1:
12                    fresh += 1
13                elif grid[r][c] == 2:
14                    rotten.append((r, c))
15        
16        while rotten and fresh > 0:
17            for _ in range(len(rotten)):
18                r, c = rotten.popleft()
19                for dr, dc in directions:
20                    nr, nc = r + dr, c + dc
21                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
22                        fresh -= 1
23                        grid[nr][nc] = 2
24                        rotten.append((nr, nc))
25            time += 1
26        
27        return time if fresh == 0 else -1