# Last updated: 11/22/2025, 2:05:02 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return 1
            return dp(i - 1) + dp(i - 2)
        
        return dp(n)