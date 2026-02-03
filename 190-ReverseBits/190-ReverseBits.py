# Last updated: 2/3/2026, 10:30:23 AM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        res = 0
4        
5        for i in range(32):
6            res <<= 1
7            res |= (n & 1)
8            n >>= 1
9        
10        return res