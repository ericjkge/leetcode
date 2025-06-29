# Last updated: 6/29/2025, 5:30:33 PM
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dp(i): # max profit from job i to end
            if i == len(intervals):
                return 0

            if i in cache:
                return cache[i]

            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(dp(i + 1), dp(j) + intervals[i][2])
            return cache[i]

        return dp(0)
