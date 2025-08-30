# Last updated: 8/29/2025, 11:18:34 PM
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.cap = k
        self.heap = []
        for n in nums:
            heapq.heappush(self.heap, n)
            if len(self.heap) > self.cap:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.cap:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)