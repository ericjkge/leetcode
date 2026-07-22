# Last updated: 7/21/2026, 7:59:26 PM
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        stack = []
4
5        for a in asteroids:
6            while stack and a < 0 < stack[-1]:
7                if stack[-1] < -a:
8                    stack.pop()
9                elif stack[-1] == -a:
10                    stack.pop()
11                    break
12                else:
13                    break
14            else:
15                stack.append(a)
16
17        return stack