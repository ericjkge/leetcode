# Last updated: 5/20/2026, 11:01:49 AM
1class Solution:
2    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
3        events = []
4
5        for l, r, h in buildings:
6            events.append((l, -h, r))
7            events.append((r, 0, 0))
8        
9        events.sort()
10
11        heap = [(0, float("inf"))]
12        res = []
13        prev = 0
14
15        for x, h, r in events:
16            if h < 0:
17                heapq.heappush(heap, (h, r))
18            
19            while heap[0][1] <= x:
20                heapq.heappop(heap)
21            
22            curr = -heap[0][0]
23            if curr != prev:
24                res.append([x, curr])
25                prev = curr
26        
27        return res
28