# Last updated: 12/26/2025, 11:36:29 PM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        seen = set()
4        num = n
5
6        while num not in seen:
7            digits = []
8            seen.add(num)
9            while num:
10                digits.append(num % 10)
11                num //= 10
12            
13            total = sum(d ** 2 for d in digits)
14            
15            if total == 1:
16                return True
17            
18            num = total
19
20        return False