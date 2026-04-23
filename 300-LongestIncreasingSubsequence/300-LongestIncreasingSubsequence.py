# Last updated: 4/23/2026, 9:55:06 AM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        @cache
4        def dp(i):
5            longest = 1
6            for j in range(i, len(nums)):
7                if nums[j] > nums[i]:
8                    longest = max(longest, 1 + dp(j))
9            return longest
10        
11        return max(dp(i) for i in range(len(nums)))