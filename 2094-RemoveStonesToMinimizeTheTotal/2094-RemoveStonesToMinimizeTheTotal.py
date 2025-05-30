# Last updated: 5/30/2025, 12:07:23 PM
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)
        
        for _ in range(k):
            largest = -heapq.heappop(heap)
            remove = largest // 2
            heapq.heappush(heap, -(largest - remove))
        return -sum(heap)