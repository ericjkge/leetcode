# Last updated: 12/28/2025, 10:24:54 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        heap = []
4        for num in nums:
5            heapq.heappush(heap, -num)
6        
7        for _ in range(k - 1):
8            heapq.heappop(heap)
9
10        return -heapq.heappop(heap)