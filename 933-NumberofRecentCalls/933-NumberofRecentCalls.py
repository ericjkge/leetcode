# Last updated: 7/22/2026, 8:30:49 PM
1class RecentCounter:
2
3    def __init__(self):
4        self.pings = deque()
5
6    def ping(self, t: int) -> int:
7        self.pings.append(t)
8        while self.pings[0] < t - 3000:
9            self.pings.popleft()
10        
11        return len(self.pings)
12
13
14# Your RecentCounter object will be instantiated and called as such:
15# obj = RecentCounter()
16# param_1 = obj.ping(t)