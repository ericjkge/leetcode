# Last updated: 2/7/2026, 1:47:47 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        heap = [-num for num in nums]
4        heapq.heapify(heap)
5
6        for _ in range(k - 1):
7            heapq.heappop(heap)
8
9        return -heapq.heappop(heap)