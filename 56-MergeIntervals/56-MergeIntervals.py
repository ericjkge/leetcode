# Last updated: 3/5/2026, 9:37:52 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        prev = None
5        res = []
6
7        for start, end in intervals:
8            if prev is not None and start <= prev:
9                res[-1][1] = max(res[-1][1], end)
10                prev = res[-1][1]
11            else:
12                res.append([start, end])
13                prev = end
14        
15        return res