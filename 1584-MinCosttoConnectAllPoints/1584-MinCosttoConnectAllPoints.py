# Last updated: 12/24/2025, 10:34:26 AM
1class Solution:
2    def minCostConnectPoints(self, points: List[List[int]]) -> int:
3        n = len(points)
4        seen = set()
5        heap = [(0, 0)]
6        cost = 0
7
8        while heap:
9            w, u = heapq.heappop(heap)
10            if u in seen:
11                continue
12            seen.add(u)
13            cost += w
14            for v in range(n):
15                if v not in seen:
16                    heapq.heappush(heap, (abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1]), v))
17
18        return cost
19