# Last updated: 1/7/2026, 11:49:47 AM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        cars = sorted(zip(position, speed), reverse=True)
4        stack = []
5
6        for p, s in cars:
7            time = (target - p) / s
8            stack.append(time)
9
10            if len(stack) > 1 and stack[-1] <= stack[-2]:
11                stack.pop()
12        
13        return len(stack)