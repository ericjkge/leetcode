# Last updated: 8/29/2025, 10:36:37 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap, -n)
        
        for _ in range(k - 1):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)