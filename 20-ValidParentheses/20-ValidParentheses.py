# Last updated: 2/28/2026, 9:56:11 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        mappings = {
4            ")":"(",
5            "}":"{",
6            "]":"["
7        }
8        stack = []
9
10        for char in s:
11            if char in mappings:
12                if stack and stack[-1] == mappings[char]:
13                    stack.pop()
14                else:
15                    return False
16            else:
17                stack.append(char)
18        
19        return not stack