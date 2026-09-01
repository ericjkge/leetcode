# Last updated: 9/1/2026, 7:16:44 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        prev = None
4        intervals.sort()
5        res = []
6
7        for start, end in intervals:
8            if prev is None or start > prev:
9                prev = end
10                res.append([start, end])
11            else:
12                prev = max(prev, end)
13                res[-1][1] = prev
14        
15        return res