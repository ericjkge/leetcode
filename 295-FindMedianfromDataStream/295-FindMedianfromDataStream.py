# Last updated: 1/2/2026, 8:37:06 PM
1class MedianFinder:
2
3    def __init__(self):
4        self.lower = [] # max heap
5        self.upper = [] # min heap
6
7    def addNum(self, num: int) -> None:
8        heapq.heappush(self.lower, -num)
9        top = -heapq.heappop(self.lower)
10        heapq.heappush(self.upper, top)
11
12        if len(self.lower) < len(self.upper):
13            bottom = heapq.heappop(self.upper)
14            heapq.heappush(self.lower, -bottom)
15
16    def findMedian(self) -> float:
17        if len(self.lower) == len(self.upper):
18            return (-self.lower[0] + self.upper[0]) / 2
19        return -self.lower[0]
20
21
22# Your MedianFinder object will be instantiated and called as such:
23# obj = MedianFinder()
24# obj.addNum(num)
25# param_2 = obj.findMedian()