# Last updated: 7/19/2025, 10:34:42 PM
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canGet(C):
            count = 0
            for pile in candies:
                count += pile // C
            return count >= k
        
        left, right = 0, max(candies)
        while left < right:
            mid = left + (right - left + 1) // 2
            if canGet(mid):
                left = mid
            else:
                right = mid - 1
        
        return left