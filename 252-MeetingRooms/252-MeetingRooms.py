# Last updated: 7/31/2025, 11:22:33 PM
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        for i in range(len(intervals)):
            start, end = intervals[i]
            if i > 0 and start < intervals[i - 1][1]:
                return False
        
        return True