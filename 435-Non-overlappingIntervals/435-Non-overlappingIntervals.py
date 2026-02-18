# Last updated: 2/18/2026, 3:08:05 PM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x: x[1])
4        prev = None
5        count = 0
6
7        for start, end in intervals:
8            if prev is not None and start < prev:
9                count += 1
10                continue
11            prev = end
12
13        return count