# Last updated: 1/9/2026, 11:07:58 AM
1class TimeMap:
2
3    def __init__(self):
4        self.dict = defaultdict(list)
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        self.dict[key].append((value, timestamp))
8
9    def get(self, key: str, timestamp: int) -> str:    
10        if key not in self.dict or self.dict[key][0][1] > timestamp:
11            return ""
12        
13        options = self.dict[key]
14        left, right = 0, len(options) - 1
15        while left + 1 < right:
16            mid = (left + right) // 2
17            if options[mid][1] < timestamp:
18                left = mid
19            else:
20                right = mid
21
22        if options[right][1] <= timestamp:
23            return options[right][0]
24        return options[left][0]
25
26
27# Your TimeMap object will be instantiated and called as such:
28# obj = TimeMap()
29# obj.set(key,value,timestamp)
30# param_2 = obj.get(key,timestamp)