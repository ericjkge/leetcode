# Last updated: 5/7/2026, 12:55:00 PM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        total = sum(nums)
4        if total % 2 != 0:
5            return False
6        target = total // 2
7
8        @cache
9        def dp(i, j):
10            if j > target or i == len(nums):
11                return False
12
13            if j == target:
14                return True
15            
16            return dp(i + 1, j + nums[i]) or dp(i + 1, j)
17        
18        return dp(0, 0)
19