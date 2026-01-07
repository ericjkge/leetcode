# Last updated: 1/7/2026, 10:54:16 AM
1class Solution:
2    def getSum(self, a: int, b: int) -> int:
3        mask = 0xFFFFFFFF
4
5        while b != 0:
6            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
7        
8        return a if a <= 0x7FFFFFFF else ~(a ^ mask)