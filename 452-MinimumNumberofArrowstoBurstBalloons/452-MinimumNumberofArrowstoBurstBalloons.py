# Last updated: 8/27/2026, 3:52:39 PM
1class Solution:
2    def findMinArrowShots(self, points: List[List[int]]) -> int:
3        prev = None
4        count = 0
5        points.sort()
6        print(points)
7
8        for start, end in points:
9            if prev is None or start > prev:
10                count += 1
11                prev = end
12            else:
13                prev = min(prev, end)
14
15        return count