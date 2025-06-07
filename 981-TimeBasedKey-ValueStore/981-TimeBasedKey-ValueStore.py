# Last updated: 6/7/2025, 2:37:48 PM
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.hashmap[key]:
            self.hashmap[key] = [(value, timestamp)]
        else:
            self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.hashmap[key] or timestamp < self.hashmap[key][0][1]:
            return ""

        left = 0
        right = len(self.hashmap[key])
        pairs = self.hashmap[key]
        while left < right:
            mid = (left + right) // 2
            if pairs[mid][1] > timestamp:
                right = mid
            else:
                left = mid + 1
        return pairs[right - 1][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)