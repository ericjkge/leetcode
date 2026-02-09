# Last updated: 2/9/2026, 4:50:45 PM
1class Solution:
2    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
3        intervals.sort()
4        prev = None
5
6        for start, end in intervals:
7            if prev and start < prev:
8                return False
9            prev = end
10        
11        return True