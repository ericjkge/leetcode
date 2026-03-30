# Last updated: 3/29/2026, 8:46:45 PM
1class Solution:
2    def minCostConnectPoints(self, points: List[List[int]]) -> int:
3        seen = set()
4        heap = [(0, 0)]
5        cost = 0
6
7        while heap:
8            w, u = heapq.heappop(heap)
9            if u in seen:
10                continue
11            seen.add(u)
12            cost += w
13            for v in range(len(points)):
14                # if v not in seen:
15                heapq.heappush(heap, (abs(points[v][0] - points[u][0]) + abs(points[v][1] - points[u][1]), v))
16        
17        return cost
18