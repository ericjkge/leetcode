# Last updated: 7/30/2025, 2:13:36 PM
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if self.k > len(self.heap) or self.heap[0] < val:
            heapq.heappush(self.heap, val)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)