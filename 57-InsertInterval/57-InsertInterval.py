# Last updated: 1/25/2026, 7:21:05 AM
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
11        while index < n and intervals[index][0] <= newInterval[1]:
12            newInterval[0] = min(newInterval[0], intervals[index][0])
13            newInterval[1] = max(newInterval[1], intervals[index][1])
14            index += 1
15        results.append(newInterval)
16
17        while index < n:
18            results.append(intervals[index])
19            index += 1
20        
21        return results