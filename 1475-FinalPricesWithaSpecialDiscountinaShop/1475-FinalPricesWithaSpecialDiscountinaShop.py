# Last updated: 7/7/2025, 10:20:14 AM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # remove next smallest value from current
        left = 0
        ans = []
        while left < len(prices):
            flag = True
            for right in range(left + 1, len(prices)):
                if prices[right] <= prices[left]:
                    ans.append(prices[left] - prices[right])
                    flag = False
                    break
            if flag:
                ans.append(prices[left])
            left += 1
        return ans
        # [8 12 18 20 23]