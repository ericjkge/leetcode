# Last updated: 8/13/2025, 12:18:12 AM
class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        ans = 0
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)

        while x:
            ans = ans * 10 + x % 10
            if ans > MAX:
                return 0
            x //= 10
        
        return sign * ans