# Last updated: 1/20/2026, 12:09:50 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        best = nums[0]
4        curr = nums[0]
5
6        for num in nums[1:]:
7            if curr < 0:
8                curr = 0
9            curr += num
10            best = max(best, curr)
11        
12        return best