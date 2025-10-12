# Last updated: 10/12/2025, 10:37:46 AM
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == curr_end:
                curr_end = farthest
                jumps += 1
        
        return jumps