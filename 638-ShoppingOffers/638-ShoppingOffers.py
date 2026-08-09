# Last updated: 8/9/2026, 11:37:34 AM
1class Solution:
2    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
3        @cache
4        def dfs(needs):
5            best = sum(price * need for price, need in zip(price, needs))
6            for offer in special:
7                remaining = tuple(need - item for need, item in zip(needs, offer[:-1]))
8                if all(x >= 0 for x in remaining):
9                    best = min(best, offer[-1] + dfs(remaining))
10            return best
11
12        return dfs(tuple(needs))