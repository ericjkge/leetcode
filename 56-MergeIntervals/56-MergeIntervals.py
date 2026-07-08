# Last updated: 7/8/2026, 12:51:51 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        merged = []
4        intervals.sort()
5
6        for start, end in intervals:
7            if merged and merged[-1][1] >= start:
8                merged[-1][1] = max(merged[-1][1], end)
9            else:
10                merged.append([start, end])
11            
12        return merged