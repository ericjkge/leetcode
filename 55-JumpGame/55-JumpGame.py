# Last updated: 10/20/2025, 2:14:18 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0


        # farthest = 0
        # for i, num in enumerate(nums):
        #     if i > farthest:
        #         return False
        #     farthest = max(farthest, i + num)
        # return True

        # n = len(nums)

        # @cache
        # def dp(i):
        #     if i >= n - 1:
        #         return True
        #     for j in range(1, nums[i] + 1):
        #         if dp(i + j):
        #             return True
        #     return False

        # return dp(0)