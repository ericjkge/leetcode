# Last updated: 7/19/2025, 9:58:49 PM
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def canFinish(T):
            return sum(T // t for t in time) >= totalTrips
        
        left, right = 0, min(time) * totalTrips
        while left < right:
            mid = left + (right - left) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        return left