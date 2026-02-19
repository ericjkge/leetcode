# Last updated: 2/19/2026, 9:34:01 AM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        heap = []
4
5        for x, y in points:
6            distance = (x**2 + y**2)**0.5
7            heapq.heappush(heap, (-distance, x, y))
8        
9        while len(heap) > k:
10            heapq.heappop(heap)
11        
12        return [[x, y] for _, x, y in heap]