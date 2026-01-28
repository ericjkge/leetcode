# Last updated: 1/28/2026, 9:31:43 AM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        max_heap = [-stone for stone in stones]
4        heapq.heapify(max_heap)
5
6        while len(max_heap) > 1:
7            s1, s2 = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
8            if s1 == s2:
9                continue
10            heapq.heappush(max_heap, -(s1 - s2))
11        
12        return -max_heap[0] if max_heap else 0