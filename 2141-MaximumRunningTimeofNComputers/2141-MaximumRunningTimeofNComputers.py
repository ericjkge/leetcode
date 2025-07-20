# Last updated: 7/20/2025, 12:37:17 PM
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def canRun(time):
            total = 0
            for battery in batteries:
                total += min(battery, time)
            return total >= n * time
        
        left, right = 0, sum(batteries) // n
        while left < right:
            mid = left + (right - left + 1) // 2
            if canRun(mid):
                left = mid
            else:
                right = mid - 1
        return left
