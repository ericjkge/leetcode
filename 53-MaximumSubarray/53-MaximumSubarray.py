# Last updated: 3/4/2026, 2:22:47 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        window = 0
4        ans = float("-inf")
5
6        for i in range(len(nums)):
7            window += nums[i]
8            ans = max(ans, window)
9
10            if window < 0:
11                window = 0
12            
13        return ans
14
15