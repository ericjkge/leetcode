# Last updated: 6/29/2025, 5:34:07 PM
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        memo = {}
        def dp(i):
            if i == len(intervals):
                return 0
            
            if i in memo:
                return memo[i]

            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            memo[i] = max(dp(i + 1), dp(j) + intervals[i][2])
            return memo[i]
        
        return dp(0)