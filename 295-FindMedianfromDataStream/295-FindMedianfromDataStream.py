# Last updated: 7/14/2026, 9:53:17 PM
1class MedianFinder:
2
3    def __init__(self):
4        self.top = []
5        self.bottom = []
6
7    def addNum(self, num: int) -> None:
8        heapq.heappush(self.bottom, -num)
9        
10        if self.top and -self.bottom[0] > self.top[0]:
11            x, y = -heapq.heappop(self.bottom), heapq.heappop(self.top)
12            heapq.heappush(self.top, x)
13            heapq.heappush(self.bottom, -y)
14
15        if len(self.bottom) > len(self.top) + 1:
16            heapq.heappush(self.top, -heapq.heappop(self.bottom))
17
18    def findMedian(self) -> float:
19        if len(self.bottom) == len(self.top):
20            return (-self.bottom[0] + self.top[0]) / 2
21        return -self.bottom[0]
22        
23        
24
25
26# Your MedianFinder object will be instantiated and called as such:
27# obj = MedianFinder()
28# obj.addNum(num)
29# param_2 = obj.findMedian()