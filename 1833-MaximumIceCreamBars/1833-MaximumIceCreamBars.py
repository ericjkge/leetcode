# Last updated: 6/21/2026, 3:23:27 PM
1class Solution:
2    def maxIceCream(self, costs: List[int], coins: int) -> int:
3        count = 0
4        for cost in sorted(costs):
5            if cost > coins:
6                break
7
8            count += 1
9            coins -= cost
10        
11        return count