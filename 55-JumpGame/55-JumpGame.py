# Last updated: 1/24/2026, 10:26:25 AM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        farthest = 0
4        curr_end = 0
5
6        for i in range(len(nums)):
7            farthest = max(farthest, i + nums[i])
8
9            if i == curr_end:
10                curr_end = farthest
11
12            if i > curr_end:
13                return False
14
15        return True