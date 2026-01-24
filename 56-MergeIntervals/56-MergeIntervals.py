# Last updated: 1/24/2026, 10:33:04 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        results = []
4        intervals.sort()
5
6        for start, end in intervals:
7            if results and start <= results[-1][1]:
8                results[-1][1] = max(end, results[-1][1])
9            else:
10                results.append([start, end])    
11
12        return results