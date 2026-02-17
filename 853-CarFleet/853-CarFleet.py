# Last updated: 2/17/2026, 9:39:38 AM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pairs = sorted(zip(position, speed), reverse=True)
4        times = []
5
6        for position, speed in pairs:
7            distance = target - position
8            time = distance / speed
9            if times and time <= times[-1]:
10                continue
11            times.append(time)
12
13        return len(times)