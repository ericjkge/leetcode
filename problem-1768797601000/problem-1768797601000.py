# Last updated: 1/19/2026, 12:40:01 PM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        farthest = 0
4        curr_end = 0
5        jumps = 0
6
7        for i in range(len(nums) - 1):
8            farthest = max(farthest, i + nums[i])
9
10            if i == curr_end:
11                jumps += 1
12                curr_end = farthest
13        
14        return jumps