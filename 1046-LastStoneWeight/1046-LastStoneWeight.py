# Last updated: 3/10/2026, 8:04:58 PM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        heap = [-stone for stone in stones]
4        heapq.heapify(heap)
5
6        while len(heap) > 1:
7            s1 = -heapq.heappop(heap)
8            s2 = -heapq.heappop(heap)
9            if s1 == s2:
10                continue
11            heapq.heappush(heap, -(s1 - s2))
12        
13        return -heap[0] if heap else 0