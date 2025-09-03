# Last updated: 9/3/2025, 10:43:04 AM
class Solution:
    def fib(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            return dp(i - 1) + dp(i - 2)
        
        return dp(n)
            