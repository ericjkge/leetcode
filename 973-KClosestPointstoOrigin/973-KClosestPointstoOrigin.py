# Last updated: 7/30/2025, 2:24:47 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (-dist, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point[1] for point in heap]