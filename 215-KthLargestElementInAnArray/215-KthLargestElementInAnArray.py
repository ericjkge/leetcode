# Last updated: 5/30/2025, 12:07:59 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for _ in range(k-1):
            heapq.heappop(heap)
        return -heap[0]
            