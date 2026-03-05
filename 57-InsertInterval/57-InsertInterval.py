# Last updated: 3/5/2026, 10:04:48 AM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        index = 0
4        res = []
5
6        while index < len(intervals) and newInterval[0] > intervals[index][1]:
7            res.append(intervals[index])
8            index += 1
9        
10        res.append(newInterval)
11
12        while index < len(intervals) and res[-1][1] >= intervals[index][0]:
13            start = min(res[-1][0], intervals[index][0])
14            end = max(res[-1][1], intervals[index][1])
15            res[-1] = [start, end]
16            index += 1
17        
18        while index < len(intervals):
19            res.append(intervals[index])
20            index += 1
21
22        return res
23        
24
25