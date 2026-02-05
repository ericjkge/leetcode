# Last updated: 2/5/2026, 8:39:12 AM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        counter = 0
4
5        while n:
6            counter += n & 1
7            n >>= 1
8        
9        return counter