# Last updated: 11/6/2026, 6:08:50 PM
1class Solution:
2    def findKthLargest(self, nums: list[int], k: int) -> int:
3        heap = [-num for num in nums]
4        heapq.heapify(heap)
5
6        for _ in range(k - 1):
7            heapq.heappop(heap)
8        
9        return -heap[0]