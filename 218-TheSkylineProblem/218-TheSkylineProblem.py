# Last updated: 5/20/2026, 10:44:45 AM
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
12        prev = 0
13        res = []
14        
15        for x, h, r in events:
16            heapq.heappush(heap, (h, r))
17            while heap[0][1] <= x:
18                heapq.heappop(heap)
19            
20            curr = -heap[0][0]
21            if curr != prev:
22                res.append([x, curr])
23                prev = curr
24        
25        return res
26
27        