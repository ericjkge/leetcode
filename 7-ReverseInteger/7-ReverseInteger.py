# Last updated: 8/13/2025, 12:23:04 AM
class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        ans = 0
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)

        while x:
            d = x % 10
            x //= 10
            if ans > MAX // 10 or (ans == MAX // 10 and d > (7 if sign == 1 else 8)):
                return 0
            ans = ans * 10 + d

        return sign * ans