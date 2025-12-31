# Last updated: 12/31/2025, 11:01:02 AM
1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        self.heap = nums
5        self.k = k
6        heapq.heapify(self.heap)
7        while len(self.heap) > self.k:
8            heapq.heappop(self.heap)
9
10    def add(self, val: int) -> int:
11        heapq.heappush(self.heap, val)
12        while len(self.heap) > self.k:
13            heapq.heappop(self.heap)
14        return self.heap[0]
15
16# Your KthLargest object will be instantiated and called as such:
17# obj = KthLargest(k, nums)
18# param_1 = obj.add(val)