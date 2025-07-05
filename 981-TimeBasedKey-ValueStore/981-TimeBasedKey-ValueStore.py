# Last updated: 7/5/2025, 11:48:58 AM
class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        
        vals = self.dict[key]

        if timestamp < vals[0][1]:
            return ""

        left = 0
        right = len(vals) - 1

        while left <= right:
            mid = (left + right) // 2
            if vals[mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return vals[right][0]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)