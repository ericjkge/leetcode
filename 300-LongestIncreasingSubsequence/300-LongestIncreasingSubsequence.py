# Last updated: 7/16/2026, 9:35:14 AM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        @cache
4        def dp(i):
5            longest = 1
6            for j in range(i):
7                if nums[i] > nums[j]:
8                    longest = max(longest, 1 + dp(j))
9            return longest
10
11        return max(dp(i) for i in range(len(nums)))