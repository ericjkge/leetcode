# Last updated: 5/20/2026, 10:44:42 AM
1class Solution:
2    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
3        events = []
4
5        for l, r, h in buildings:
6            events.append((l, -h, r))
7            events.append((r, 0, 0))
8        
9        events.sort()
10        print(events)
11
12        heap = [(0, float("inf"))]
13        prev = 0
14        res = []
15        
16        for x, h, r in events:
17            heapq.heappush(heap, (h, r))
18            while heap[0][1] <= x:
19                heapq.heappop(heap)
20            
21            curr = -heap[0][0]
22            if curr != prev:
23                res.append([x, curr])
24                prev = curr
25        
26        return res
27
28        