# Last updated: 7/4/2025, 11:04:47 AM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        seen = set()

        for num, freq in counter.items():
            if freq in seen:
                return False
            seen.add(freq)
        
        return True
        