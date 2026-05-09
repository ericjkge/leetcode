# Last updated: 5/9/2026, 10:17:10 AM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        heap = []
4
5        for x, y in points:
6            distance = x ** 2 + y ** 2
7            heapq.heappush(heap, (distance, x, y))
8        
9        closest = []
10        for i in range(k):
11            _, x, y = heapq.heappop(heap)
12            closest.append((x, y))
13        
14        return closest