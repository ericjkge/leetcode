# Last updated: 6/17/2026, 7:32:11 PM
1class Solution:
2    def angleClock(self, hour: int, minutes: int) -> float:
3        hour_angle = hour / 12 * 360 % 360 + minutes / 60 * 30
4        minutes_angle = minutes / 60 * 360
5
6        difference = abs(minutes_angle - hour_angle)
7        return min(difference, 360 - difference)
8