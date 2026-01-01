# Last updated: 1/1/2026, 9:33:41 AM
1class Solution:
2    def swimInWater(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        distances = [[float("inf") for _ in range(n)] for _ in range(n)]
5        distances[0][0] = grid[0][0]
6        heap = [(grid[0][0], 0, 0)] # 0, source
7        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
8
9        while heap:
10            dist, r, c = heapq.heappop(heap)
11
12            if r == n - 1 and c == n - 1:
13                return dist
14
15            if dist > distances[r][c]:
16                continue
17            
18            for dr, dc in directions:
19                nr, nc = r + dr, c + dc
20                if 0 <= nr < n and 0 <= nc < n and distances[nr][nc] > dist + grid[nr][nc]:
21                    new_dist = max(dist, grid[nr][nc])
22                    if new_dist < distances[nr][nc]:
23                        distances[nr][nc] = new_dist
24                        heapq.heappush(heap, (new_dist, nr, nc))
25        
26        return max(max(distances[r]) for r in range(n))
27
28