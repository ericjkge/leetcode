# Last updated: 7/5/2026, 11:54:05 PM
1class Solution:
2    def countGoodNumbers(self, n: int) -> int:
3        MOD = 10**9 + 7
4        
5        even_count = (n + 1) // 2
6        odd_count = n // 2
7        
8        choices_even = pow(5, even_count, MOD)
9        choices_odd = pow(4, odd_count, MOD)
10        
11        return (choices_even * choices_odd) % MOD