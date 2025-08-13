# Last updated: 8/14/2025, 12:14:40 AM
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]

        @cache
        def dp(num):
            if num == 0:
                return 0
            
            root = int(num ** 0.5)
            if root * root == num:
                return 1

            return 1 + min(dp(num - square) for square in squares if square <= num)

        return dp(n)