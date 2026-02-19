# Last updated: 2/19/2026, 9:53:35 AM
1class TimeMap:
2
3    def __init__(self):
4        self.storage = defaultdict(list) # k : [(v1, t1), (v2, t2), ...]
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        self.storage[key].append((value, timestamp))
8
9    def get(self, key: str, timestamp: int) -> str:
10        if key not in self.storage or self.storage[key][0][1] > timestamp:
11            return ""
12
13        left, right = 0, len(self.storage[key]) - 1
14        while left + 1 < right:
15            mid = (left + right) // 2
16            if self.storage[key][mid][1] > timestamp:
17                right = mid
18            else:
19                left = mid
20        
21        if self.storage[key][right][1] <= timestamp:
22            return self.storage[key][right][0]
23        return self.storage[key][left][0]
24
25
26# Your TimeMap object will be instantiated and called as such:
27# obj = TimeMap()
28# obj.set(key,value,timestamp)
29# param_2 = obj.get(key,timestamp)