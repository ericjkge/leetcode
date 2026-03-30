# Last updated: 3/30/2026, 9:20:20 AM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        bits = 0
4
5        while n:
6            bits += (n & 1)
7            n >>= 1
8        
9        return bits