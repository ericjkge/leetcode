# Last updated: 7/2/2025, 2:23:56 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            heapq.heappush(heap, (x ** 2 + y ** 2, (x, y)))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans