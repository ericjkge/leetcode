# Last updated: 2/27/2026, 8:39:19 AM
1class Solution:
2    def reverse(self, x: int) -> int:
3        MIN = -2**31
4        MAX = 2**31 - 1
5        rev = 0
6        sign = 1
7
8        if x < 0:
9            sign = -1
10            x *= -1
11
12        while x:
13            rev *= 10
14            rev += x % 10
15            x //= 10
16        
17        rev *= sign
18
19        return rev if MIN <= rev <= MAX else 0