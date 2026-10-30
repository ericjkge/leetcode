# Last updated: 10/30/2026, 11:33:19 AM
1class Solution:
2    def increasingTriplet(self, nums: list[int]) -> bool:
3        f1 = f2 = f3 = None
4
5        for num in nums:
6            if f1 is None or num <= f1:
7                f1 = num
8            elif f2 is None or num <= f2:
9                f2 = num
10            elif f3 is None:
11                f3 = num
12                break
13            
14        return f1 is not None and f2 is not None and f3 is not None