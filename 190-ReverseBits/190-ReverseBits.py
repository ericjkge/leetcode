# Last updated: 3/30/2026, 9:16:16 AM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        reversed = 0
4
5        for i in range(32):
6            reversed <<= 1
7            reversed |= (n&1)
8            n >>= 1
9        
10        return reversed