# Last updated: 1/25/2026, 7:11:47 AM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        index = 0
4        results = []
5        n = len(intervals)
6
7        while index < n and intervals[index][1] < newInterval[0]:
8            results.append(intervals[index])
9            index += 1
10
11        if index < n and intervals[index][0] <= newInterval[1]:
12            start, end = min(intervals[index][0], newInterval[0]), max(intervals[index][1], newInterval[1])
13            index += 1
14        else:
15            start, end = newInterval[0], newInterval[1]
16        results.append([start, end])
17
18
19        while index < n and intervals[index][0] <= end:
20            results[-1][1] = max(intervals[index][1], end)
21            index += 1
22        
23        while index < n:
24            results.append(intervals[index])
25            index += 1
26        
27        return results