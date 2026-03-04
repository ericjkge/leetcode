# Last updated: 3/4/2026, 2:22:11 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        left = right = 0
4        window = 0
5        ans = float("-inf")
6
7        while right < len(nums):
8            window += nums[right]
9            ans = max(ans, window)
10
11            if window < 0:
12                window = 0
13                left = right + 1
14
15            right += 1
16            
17        return ans
18
19