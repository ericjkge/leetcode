# Last updated: 8/8/2025, 11:01:53 PM
class Solution:
    def fib(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 0 or i == 1:
                return i
            
            return dp(i - 1) + dp(i - 2)

        return dp(n)