# Last updated: 1/25/2026, 7:33:32 AM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n = len(s2)
4        letters = Counter(s1)
5        start, end = 0, len(s1)
6
7        while end < n + 1:
8            if letters == Counter(s2[start:end]):
9                return True
10            start += 1
11            end += 1
12
13        return False