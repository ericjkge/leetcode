# Last updated: 7/22/2026, 8:25:52 PM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        string = ""
4        stack = []
5        num = 0
6
7        for c in s:
8            if c.isdigit():
9                num = num * 10 + int(c)
10            elif c == "[":
11                stack.append((string, num))
12                num = 0
13                string = ""
14            elif c == "]":
15                prev, repeats = stack.pop()
16                string = prev + repeats * string
17            else:
18                string += c
19        
20        return string