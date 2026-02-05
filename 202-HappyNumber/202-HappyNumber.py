# Last updated: 2/5/2026, 9:18:24 AM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        seen = set()
4
5        while True:
6            nxt = 0
7            while n:
8                digit = n % 10
9                nxt += digit ** 2
10                n //= 10
11            if nxt in seen:
12                break
13            seen.add(nxt)
14            n = nxt
15        
16        if 1 in seen:
17            return True
18        return False