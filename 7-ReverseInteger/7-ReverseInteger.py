# Last updated: 1/14/2026, 11:25:41 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        MAX = 2 ** 31 - 1
4        MIN = -2 ** 31
5
6        flag = 1 if x >= 0 else -1
7        x = abs(x)
8        reverse = 0
9
10        while x:
11            reverse *= 10
12            reverse += x % 10
13            x //= 10
14            if reverse > MAX or reverse < MIN:
15                return 0
16        
17        return reverse * flag
18