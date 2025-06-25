# Last updated: 6/24/2025, 10:28:20 PM
# Two heaps
class MedianFinder:

    def __init__(self):
        self.small = [] # the smaller half of the list, max heap
        self.large = [] # the larger half of the list
        
    # Alltogether, the add operation is O(logn), The findMedian operation is O(1).
    def addNum(self, num: int) -> None:
        # 1, 2, 3
        # 1, 2
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num)) # large [1], [2, 3]
            # print("---large----")
            # print(self.large)
        else:
            heappush(self.small, -heappushpop(self.large, num)) # small [-1]
            # print("---samll----")
            # print(self.small)
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()