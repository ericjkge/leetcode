# Last updated: 3/3/2026, 9:07:58 AM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        def binExp(b, p):
4            if p == 0:
5                return 1
6            
7            if p < 0:
8                return 1/binExp(b, -p)
9
10            res = binExp(b, p // 2)
11            if p % 2 == 0:
12                return res * res
13            return b * res * res
14        
15        return binExp(x, n)