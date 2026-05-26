# Last updated: 5/26/2026, 8:02:08 AM
1class Solution:
2    def addDigits(self, num: int) -> int:
3        while num >= 10:
4            res = 0
5            while num:
6                res += num % 10
7                num //= 10
8            num = res
9        
10        return num