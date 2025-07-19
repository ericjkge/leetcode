# Last updated: 7/19/2025, 11:32:07 PM
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def canGet(tastiness):
            prev, count = price[0], 1
            for i in range(len(price)):
                if price[i] - prev >= tastiness:
                    prev = price[i]
                    count += 1
            return count >= k
        
        left, right = 0, price[-1] - price[0]
        while left < right:
            mid = left + (right - left + 1) // 2
            if canGet(mid):
                left = mid
            else:
                right = mid - 1
        return left