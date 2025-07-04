# Last updated: 7/4/2025, 10:54:27 AM
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans = -1
        
        for num, freq in counter.items():
            if num == freq:
                ans = max(ans, num)
        
        return ans