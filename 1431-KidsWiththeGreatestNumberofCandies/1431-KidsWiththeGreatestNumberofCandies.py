# Last updated: 10/30/2026, 10:01:52 AM
1class Solution:
2    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
3        out = [False] * len(candies)
4        maximum = max(candies)
5
6        for i, candy in enumerate(candies):
7            if candy + extraCandies >= maximum:
8                out[i] = True
9        
10        return out