# Last updated: 7/7/2025, 10:23:48 AM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # remove next smallest value from current
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices