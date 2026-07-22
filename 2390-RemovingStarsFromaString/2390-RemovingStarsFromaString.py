# Last updated: 7/21/2026, 7:39:41 PM
1class Solution:
2    def removeStars(self, s: str) -> str:
3        stack = []
4
5        for c in s:
6            if c != "*":
7                stack.append(c)
8            else:
9                stack.pop()
10        
11        return "".join(stack)