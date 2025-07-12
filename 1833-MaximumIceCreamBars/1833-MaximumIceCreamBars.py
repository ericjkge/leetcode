# Last updated: 7/12/2025, 3:37:22 PM
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, c in enumerate(costs):
            if coins < c:
                return i
            coins -= c
        return len(costs)