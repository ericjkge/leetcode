# Last updated: 2/19/2026, 9:47:35 AM
1class TimeMap:
2
3    def __init__(self):
4        self.storage = defaultdict(list) # k : [(v1, t1), (v2, t2), ...]
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        self.storage[key].append((value, timestamp))
8
9    def get(self, key: str, timestamp: int) -> str:
10        if key in self.storage:
11            for v, t in reversed(self.storage[key]):
12                if t <= timestamp:
13                    return v
14        return ""
15
16
17# Your TimeMap object will be instantiated and called as such:
18# obj = TimeMap()
19# obj.set(key,value,timestamp)
20# param_2 = obj.get(key,timestamp)