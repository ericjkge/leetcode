# Last updated: 11/20/2025, 12:12:01 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = curr = 0
        
        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i]) 
            if i == curr:
                curr = farthest

        return curr >= len(nums) - 1

        # Option 1: Greedy (backwards)
        # goal = len(nums) - 1

        # for i in range(len(nums) - 2, -1, -1):
        #     if i + nums[i] >= goal:
        #         goal = i
        
        # return goal == 0


        # Option 2: Greedy (forwards)
        # farthest = 0
        # for i, num in enumerate(nums):
        #     if i > farthest:
        #         return False
        #     farthest = max(farthest, i + num)
        # return True


        # Option 3: DP
        # @cache
        # def dp(i):
        #     if i >= len(nums) - 1:
        #         return True
        #     for j in range(1, nums[i] + 1):
        #         if dp(i + j):
        #             return True
        #     return False

        # return dp(0)