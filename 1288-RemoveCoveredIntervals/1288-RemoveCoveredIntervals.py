# Last updated: 7/31/2025, 11:54:01 PM
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        prev_start = float("inf")
        prev_end = float("-inf")
        ans = len(intervals)
        
        for start, end in intervals:
            if prev_start <= start and end <= prev_end:
                ans -= 1
            else:
                prev_start, prev_end = start, end
        
        return ans