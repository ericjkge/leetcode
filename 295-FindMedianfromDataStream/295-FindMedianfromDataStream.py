# Last updated: 2/14/2026, 5:59:11 PM
1class MedianFinder:
2
3    def __init__(self):
4        self.lower = []
5        self.upper = []
6
7    def addNum(self, num: int) -> None:
8        heapq.heappush(self.lower, -num)
9        heapq.heappush(self.upper, -heapq.heappop(self.lower))
10
11        if len(self.lower) + 1 < len(self.upper):
12            heapq.heappush(self.lower, -heapq.heappop(self.upper))
13
14    def findMedian(self) -> float:
15        if len(self.lower) == len(self.upper):
16            return (-self.lower[0] + self.upper[0]) / 2
17        return self.upper[0]
18
19
20# Your MedianFinder object will be instantiated and called as such:
21# obj = MedianFinder()
22# obj.addNum(num)
23# param_2 = obj.findMedian()