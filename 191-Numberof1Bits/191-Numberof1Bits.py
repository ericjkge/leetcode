# Last updated: 12/26/2025, 10:29:41 PM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        counter = 0
4
5        while n:
6            if n & 1:
7                counter += 1
8            n >>= 1
9        
10        return counter