# Last updated: 1/20/2026, 11:34:50 AM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        def binExp(b, p):
4            if p == 0:
5                return 1
6            
7            if p < 0:
8                return 1/binExp(b, -p)
9            
10            if p % 2 == 1:
11                return b * binExp(b * b, (p - 1) // 2)
12            return binExp(b * b, p // 2)
13
14        return binExp(x, n)