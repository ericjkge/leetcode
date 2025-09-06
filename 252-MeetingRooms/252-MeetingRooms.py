# Last updated: 9/6/2025, 2:18:07 PM
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        prev = -float("inf")

        for start, end in intervals:
            if start < prev:
                return False
            prev = end
        
        return True