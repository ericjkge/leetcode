# Last updated: 2/17/2026, 9:38:27 AM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pairs = sorted(zip(position, speed), reverse=True)
4        times = []
5
6        for position, speed in pairs:
7            distance = target - position
8            times.append(distance / speed)
9
10        stack = []
11
12        for time in times:
13            if stack and time <= stack[-1]:
14                continue
15            stack.append(time)    
16
17        return len(stack)