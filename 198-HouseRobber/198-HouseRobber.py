# Last updated: 7/21/2025, 4:42:57 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(dp(i + 1), dp(i + 2) + nums[i])
            return memo[i]
        
        return dp(0)