# Last updated: 8/13/2025, 12:15:32 AM
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)

        while x:
            ans = ans * 10 + x % 10
            if ans > 2 ** 31 - 1:
                return 0
            x //= 10
        
        return sign * ans