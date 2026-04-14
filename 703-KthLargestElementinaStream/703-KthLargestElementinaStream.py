# Last updated: 4/14/2026, 10:05:11 AM
1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        self.k = k
5        self.heap = nums
6        heapq.heapify(self.heap)
7        while len(self.heap) > k:
8            heapq.heappop(self.heap)
9
10    def add(self, val: int) -> int:
11        heapq.heappush(self.heap, val)
12        if len(self.heap) > self.k:
13            heapq.heappop(self.heap)
14        return self.heap[0]
15
16# Your KthLargest object will be instantiated and called as such:
17# obj = KthLargest(k, nums)
18# param_1 = obj.add(val)