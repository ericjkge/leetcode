# Last updated: 1/9/2026, 11:06:10 AM
1class TimeMap:
2
3    def __init__(self):
4        self.dict = defaultdict(list)
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        self.dict[key].append((value, timestamp))
8
9    def get(self, key: str, timestamp: int) -> str:    
10        options = self.dict[key]
11        
12        if not options:
13            return ""
14            
15        left, right = 0, len(options) - 1
16        while left + 1 < right:
17            mid = (left + right) // 2
18            if options[mid][1] < timestamp:
19                left = mid
20            else:
21                right = mid
22
23        if options[right][1] <= timestamp:
24            return options[right][0]
25        elif options[left][1] <= timestamp: 
26            return options[left][0]
27        return ""
28
29# Your TimeMap object will be instantiated and called as such:
30# obj = TimeMap()
31# obj.set(key,value,timestamp)
32# param_2 = obj.get(key,timestamp)