# Last updated: 6/22/2026, 11:05:33 PM
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        left, right = 0, x
4
5        while left + 1 < right:
6            mid = (left + right) // 2
7            if mid * mid < x:
8                left = mid
9            else:
10                right = mid
11        
12        if right * right <= x:
13            return right
14        return left