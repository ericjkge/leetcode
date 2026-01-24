# Last updated: 1/24/2026, 10:32:05 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        results = []
4        intervals.sort()
5        prev = None
6
7        for start, end in intervals:
8            if prev is not None and start <= prev:
9                results[-1][1] = max(end, prev)
10                prev = results[-1][1]
11            else:
12                results.append([start, end])    
13                prev = end
14
15        return results