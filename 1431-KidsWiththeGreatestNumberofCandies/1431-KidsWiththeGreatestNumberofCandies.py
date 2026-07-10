# Last updated: 7/9/2026, 9:11:00 PM
1class Solution:
2    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
3        mx = max(candies)
4        ans = [False] * len(candies)
5
6        for i, kid in enumerate(candies):
7            if kid + extraCandies >= mx:
8                ans[i] = True
9        
10        return ans