# Last updated: 3/5/2026, 9:38:30 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        res = []
5
6        for start, end in intervals:
7            if res and start <= res[-1][1]:
8                res[-1][1] = max(res[-1][1], end)
9            else:
10                res.append([start, end])
11        
12        return res