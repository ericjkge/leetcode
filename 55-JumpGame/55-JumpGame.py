# Last updated: 3/5/2026, 9:35:15 AM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        curr_end = farthest = 0
4
5        for i in range(len(nums)):
6            curr_end = max(curr_end, i + nums[i])
7
8            if i == farthest:
9                farthest = curr_end
10            
11        return farthest >= len(nums) - 1