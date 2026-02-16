# Last updated: 2/16/2026, 11:22:03 AM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        ones = []
4
5        for i in range(n + 1):
6            count = 0
7            while i:
8                if i & 1:
9                    count += 1
10                i >>= 1
11            ones.append(count)
12
13        return ones