# Last updated: 2/17/2026, 9:19:14 AM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        if sum(nums) % 2 != 0:
4            return False
5        
6        target = sum(nums) // 2
7        nums.sort()
8
9        @cache
10        def dp(i, j): # position, sum
11            if j == target:
12                return True
13
14            if i == len(nums):
15                return False
16            
17            return dp(i + 1, j) or dp(i + 1, j + nums[i])
18        
19        return dp(0, 0)