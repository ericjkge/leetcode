# Last updated: 11/1/2026, 1:00:50 PM
1class Solution:
2    def largestAltitude(self, gain: list[int]) -> int:
3        highest = 0
4        prefix = 0
5
6        for g in gain:
7            prefix += g
8            highest = max(highest, prefix)
9
10        return highest