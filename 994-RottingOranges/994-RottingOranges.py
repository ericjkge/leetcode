# Last updated: 7/15/2026, 12:21:49 AM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        rows, cols = len(grid), len(grid[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5        queue = deque()
6        fresh = 0
7
8        for r in range(rows):
9            for c in range(cols):
10                if grid[r][c] == 1:
11                    fresh += 1
12                elif grid[r][c] == 2:
13                    queue.append((r, c))
14    
15        time = 0
16        while queue and fresh > 0:
17            for _ in range(len(queue)):
18                r, c = queue.popleft()
19                for dr, dc in directions:
20                    nr, nc = r + dr, c + dc
21                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
22                        fresh -= 1
23                        grid[nr][nc] = 2
24                        queue.append((nr, nc))
25            time += 1
26        
27        return time if fresh == 0 else -1