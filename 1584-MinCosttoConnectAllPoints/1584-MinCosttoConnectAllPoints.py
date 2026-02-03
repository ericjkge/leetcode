# Last updated: 2/3/2026, 10:07:20 AM
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
20
21
22        # n = len(points)
23        # seen = set()
24        # heap = [(0, 0)]
25        # cost = 0
26
27        # while heap:
28        #     w, u = heapq.heappop(heap)
29        #     if u in seen:
30        #         continue
31        #     seen.add(u)
32        #     cost += w
33        #     for v in range(n):
34        #         if v not in seen:
35        #             heapq.heappush(heap, (abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1]), v))
36
37        # return cost
38