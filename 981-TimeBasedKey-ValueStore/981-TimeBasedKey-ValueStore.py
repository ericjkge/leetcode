# Last updated: 6/28/2025, 6:43:36 PM
class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append((value, timestamp))
        else:
            self.dict[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if not self.dict[key] or timestamp < self.dict[key][0][1]:
            return ""
        
        left = 0
        right = len(self.dict[key])
        pairs = self.dict[key]
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