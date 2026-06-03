# Last updated: 6/2/2026, 8:15:24 PM
1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3        earliest = float("inf")
4
5        landEnd = min(start + duration for start, duration in zip(landStartTime, landDuration))
6        for start, duration in zip(waterStartTime, waterDuration):
7            earliest = min(earliest, max(start, landEnd) + duration)
8        
9        waterEnd = min(start + duration for start, duration in zip(waterStartTime, waterDuration))
10        for start, duration in zip(landStartTime, landDuration):
11            earliest = min(earliest, max(start, waterEnd) + duration)
12        
13        return earliest
14