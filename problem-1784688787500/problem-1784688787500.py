# Last updated: 7/21/2026, 7:53:07 PM
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        stack = []
4
5        for asteroid in asteroids:
6            if asteroid > 0:
7                stack.append(asteroid)
8            else:
9                if not stack or stack[-1] < 0:
10                    stack.append(asteroid)
11                else:
12                    append = True
13                    while stack and stack[-1] > 0:
14                        if abs(stack[-1]) > abs(asteroid):
15                            append = False
16                            break
17                        elif abs(stack[-1]) == abs(asteroid):
18                            append = False
19                            stack.pop()
20                            break
21                        elif abs(stack[-1]) < abs(asteroid):
22                            stack.pop()
23
24                    if append:
25                        stack.append(asteroid)
26
27        return stack