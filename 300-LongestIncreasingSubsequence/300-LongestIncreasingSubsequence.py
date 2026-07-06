# Last updated: 7/5/2026, 10:58:49 PM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        @cache
4        def dp(i):
5            res = 1
6            for j in range(i):
7                if nums[j] < nums[i]:
8                    res = max(res, 1 + dp(j))
9            
10            return res
11        
12        return max(dp(i) for i in range(len(nums)))