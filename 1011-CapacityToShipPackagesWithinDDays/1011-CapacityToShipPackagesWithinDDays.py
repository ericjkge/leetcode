# Last updated: 7/25/2025, 4:32:39 PM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            counter = 1
            total = 0
            for w in weights:
                if total + w <= capacity:
                    total += w
                else:
                    counter += 1
                    total = w
            return counter <= days
        
        left, right = max(weights), sum(weights)
        while left + 1 < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid
        
        if canShip(left):
            return left
        return right