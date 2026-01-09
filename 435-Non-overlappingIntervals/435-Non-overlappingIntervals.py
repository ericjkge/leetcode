# Last updated: 1/9/2026, 9:53:18 AM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x : x[1])
4        prev = float("-inf")
5        count = 0
6
7        for start, end in intervals:
8            if start < prev:
9                count += 1
10            else:
11                prev = end
12        
13        return count