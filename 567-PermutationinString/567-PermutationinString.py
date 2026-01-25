# Last updated: 1/25/2026, 7:50:09 AM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n, k = len(s2), len(s1)
4        c1 = Counter(s1)
5        c2 = Counter(s2[:k])
6
7        if c1 == c2:
8            return True
9
10        for i in range(k, n):
11            c2[s2[i]] += 1
12            c2[s2[i - k]] -= 1
13
14            if not c2[s2[i - k]]:
15                del c2[s2[i - k]]
16
17            if c1 == c2:
18                return True
19
20        return False