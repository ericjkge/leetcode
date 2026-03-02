# Last updated: 3/2/2026, 1:22:17 PM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        if len(nums) <= 1:
4            return 0
5
6        curr_end = farthest = 0
7        jumps = 0
8
9        for i in range(len(nums) - 1):
10            farthest = max(farthest, i + nums[i])
11
12            if i == curr_end:
13                jumps += 1
14                curr_end = farthest
15            
16        return jumps