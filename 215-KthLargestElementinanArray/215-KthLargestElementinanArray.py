# Last updated: 4/4/2026, 9:37:37 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        heap = [-n for n in nums]
4        heapq.heapify(heap)
5        for _ in range(k - 1):
6            heapq.heappop(heap)
7        
8        return -heapq.heappop(heap)