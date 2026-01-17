# Last updated: 1/17/2026, 11:35:26 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        mapping = {
5            "(":")",
6            "{":"}",
7            "[":"]"
8        }
9
10        for c in s:
11            if c in mapping:
12                stack.append(c)
13            elif stack and mapping[stack[-1]] == c:
14                stack.pop()
15            else:
16                return False
17        
18        return not stack
19