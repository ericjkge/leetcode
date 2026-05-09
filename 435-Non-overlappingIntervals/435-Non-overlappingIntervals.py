# Last updated: 5/8/2026, 8:58:23 PM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x: (x[1], x[0]))
4        prev = None
5        count = 0
6
7        for start, end in intervals:
8            if prev is not None and start < prev:
9                count += 1
10            else:
11                prev = end
12            
13        return count
14