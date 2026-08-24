# Last updated: 8/24/2026, 11:06:33 AM
1class Solution:
2    def minFlips(self, a: int, b: int, c: int) -> int:
3        count = 0
4
5        while a or b or c:
6            if c & 1 and not (a | b) & 1:
7                count += 1
8            elif not c & 1 and (a | b) & 1:
9                count += (a & 1) + (b & 1)
10            a >>= 1
11            b >>= 1
12            c >>= 1
13
14        return count