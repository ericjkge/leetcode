# Last updated: 11/6/2026, 10:05:47 AM
1class Solution:
2    def removeStars(self, s: str) -> str:
3        stack = []
4
5        for ch in s:
6            if ch == "*":
7                stack.pop()
8            else:
9                stack.append(ch)
10        
11        return "".join(stack)