# Last updated: 7/20/2026, 9:37:38 PM
1class Solution:
2    def uniqueOccurrences(self, arr: List[int]) -> bool:
3        counter = Counter(arr)
4
5        seen = set()
6        for value in counter.values():
7            if value in seen:
8                return False
9            seen.add(value)
10        
11        return True