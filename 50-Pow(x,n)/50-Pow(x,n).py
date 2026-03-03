# Last updated: 3/3/2026, 9:07:04 AM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        def binExp(b, p):
4            if p == 0:
5                return 1
6            
7            if p < 0:
8                return 1/binExp(b, -p)
9
10            if p % 2 == 0:
11                return binExp(b * b, p // 2)
12            return b * binExp(b * b, (p - 1) // 2)
13        
14        return binExp(x, n)