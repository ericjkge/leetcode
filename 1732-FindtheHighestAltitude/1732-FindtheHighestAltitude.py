# Last updated: 7/19/2026, 9:01:52 PM
1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        prefix = 0
4        mx = 0
5
6        for height in gain:
7            prefix += height
8            mx = max(mx, prefix)
9        
10        return mx