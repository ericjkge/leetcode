# Last updated: 9/1/2026, 7:56:30 AM
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
13            res[-1][0] = min(res[-1][0], intervals[index][0])
14            res[-1][1] = max(res[-1][1], intervals[index][1])
15            index += 1
16        
17        while index < len(intervals):
18            res.append(intervals[index])
19            index += 1
20        
21        return res
22
23
24