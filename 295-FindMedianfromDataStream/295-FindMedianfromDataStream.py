# Last updated: 9/1/2026, 10:22:25 AM
1class MedianFinder:
2
3    def __init__(self):
4        self.lower, self.upper = [], []
5
6    def addNum(self, num: int) -> None:
7        heapq.heappush(self.lower, -num)
8        heapq.heappush(self.upper, -heapq.heappop(self.lower))
9
10        if len(self.upper) > len(self.lower) + 1:
11            heapq.heappush(self.lower, -heapq.heappop(self.upper))
12
13    def findMedian(self) -> float:
14        if len(self.lower) == len(self.upper):
15            return (-self.lower[0] + self.upper[0]) / 2
16        return self.upper[0]
17
18
19# Your MedianFinder object will be instantiated and called as such:
20# obj = MedianFinder()
21# obj.addNum(num)
22# param_2 = obj.findMedian()