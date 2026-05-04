# Last updated: 5/4/2026, 12:37:58 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pairs = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
4        stack = []
5
6        for p, s in pairs:
7            time = (target - p) / s
8            if not stack or time > stack[-1]:
9                stack.append(time)
10
11        return len(stack)