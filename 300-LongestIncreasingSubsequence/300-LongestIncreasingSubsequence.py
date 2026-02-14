# Last updated: 2/14/2026, 6:09:03 PM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        @cache
6        def dp(i):
7            if i == n:
8                return 0
9            
10            ways = 1
11
12            for j in range(i + 1, n):
13                if nums[j] > nums[i]:
14                    ways = max(ways, 1 + dp(j))
15            
16            return ways
17            
18
19
20        return max(dp(i) for i in range(len(nums)))