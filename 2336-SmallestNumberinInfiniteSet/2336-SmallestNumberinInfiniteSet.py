# Last updated: 7/9/2025, 11:14:57 PM
class SmallestInfiniteSet:

    def __init__(self):
        self.marker = 1
        self.heap = []
        self.set = set()

    def popSmallest(self) -> int:
        if self.heap:
            popped = heapq.heappop(self.heap)
            self.set.remove(popped)
            return popped

        smallest = self.marker
        self.marker += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.marker and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)