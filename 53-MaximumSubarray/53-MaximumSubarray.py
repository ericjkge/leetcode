# Last updated: 1/20/2026, 11:54:10 AM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        best = float("-inf")
4        curr = 0
5
6        for num in nums:
7            curr += num
8            best = max(best, curr)
9            if curr < 0:
10                curr = 0
11
12        return best