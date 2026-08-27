# Last updated: 8/27/2026, 3:52:46 PM
1class Solution:
2    def findMinArrowShots(self, points: List[List[int]]) -> int:
3        prev = None
4        count = 0
5        points.sort()
6
7        for start, end in points:
8            if prev is None or start > prev:
9                count += 1
10                prev = end
11            else:
12                prev = min(prev, end)
13
14        return count