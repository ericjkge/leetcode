# Last updated: 4/2/2026, 9:41:37 AM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        curr = n
4        seen = set()
5
6        while True:
7            total = 0
8            while curr:
9                digit = curr % 10
10                total += digit ** 2
11                curr //= 10
12
13            if total == 1:
14                return True
15
16            if total in seen:
17                return False
18            
19            seen.add(total)
20            curr = total