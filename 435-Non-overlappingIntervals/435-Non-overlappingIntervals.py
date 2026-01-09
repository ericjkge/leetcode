# Last updated: 1/9/2026, 9:51:41 AM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x : x[1])
4        print(intervals)
5        prev = float("-inf")
6        count = 0
7
8        for start, end in intervals:
9            if start < prev:
10                count += 1
11            else:
12                prev = end
13        
14        return count