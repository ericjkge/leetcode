# Last updated: 7/14/2026, 10:58:58 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        window = 0
4        mx = float("-inf")
5
6        for num in nums:
7            if window < 0:
8                window = 0
9            
10            window += num
11            mx = max(mx, window)
12
13        return mx