# Last updated: 3/2/2026, 1:22:37 PM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        curr_end = farthest = 0
4        jumps = 0
5
6        for i in range(len(nums) - 1):
7            farthest = max(farthest, i + nums[i])
8
9            if i == curr_end:
10                jumps += 1
11                curr_end = farthest
12            
13        return jumps