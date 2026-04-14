# Last updated: 4/14/2026, 10:24:14 AM
1class Solution:
2    def swimInWater(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        heap = [(grid[0][0], 0, 0)]
5        seen = set([(0, 0)])
6        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
7
8        while heap:
9            time, r, c = heapq.heappop(heap)
10
11            if r == n - 1 and c == n - 1:
12                return time
13            
14            for dr, dc in directions:
15                nr, nc = r + dr, c + dc
16                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
17                    seen.add((nr, nc))
18                    new_time = max(time, grid[nr][nc])
19                    heapq.heappush(heap, (new_time, nr, nc))
20        
21        