# Last updated: 1/9/2026, 10:34:22 AM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        heap = []
4
5        for x, y in points:
6            distance = x ** 2 + y ** 2
7            heapq.heappush(heap, (distance, (x, y)))
8        
9        return[heapq.heappop(heap)[1] for _ in range(k)]