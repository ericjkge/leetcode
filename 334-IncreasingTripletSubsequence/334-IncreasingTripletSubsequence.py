# Last updated: 7/17/2026, 12:02:25 AM
1class Solution:
2    def increasingTriplet(self, nums: List[int]) -> bool:
3        first = second = float("inf")
4
5        for num in nums:
6            if num <= first:
7                first = num
8            elif num <= second:
9                second = num
10            else:
11                return True
12            
13        return False
14