# Last updated: 4/23/2026, 9:16:04 AM
1class MedianFinder:
2
3    def __init__(self):
4        self.lower = []
5        self.upper = []
6
7    def addNum(self, num: int) -> None:
8        heapq.heappush(self.lower, -num)
9
10        heapq.heappush(self.upper, -heapq.heappop(self.lower))
11
12        if len(self.upper) > len(self.lower) + 1:
13            heapq.heappush(self.lower, -heapq.heappop(self.upper))
14
15    def findMedian(self) -> float:
16        # print(self.lower, self.upper)
17        if len(self.lower) == len(self.upper):
18            return (-self.lower[0] + self.upper[0]) / 2
19        return self.upper[0]
20
21# Your MedianFinder object will be instantiated and called as such:
22# obj = MedianFinder()
23# obj.addNum(num)
24# param_2 = obj.findMedian()