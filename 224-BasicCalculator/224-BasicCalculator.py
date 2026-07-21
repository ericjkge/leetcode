# Last updated: 7/20/2026, 10:12:22 PM
1class Solution:
2    def calculate(self, s: str) -> int:
3        res = 0
4        sign = 1
5        num = 0
6        stack = []
7        i = 0
8
9        while i < len(s):
10            c = s[i]
11            if c.isdigit():
12                num = 0
13                while i < len(s) and s[i].isdigit():
14                    num = num * 10 + int(s[i])
15                    i += 1
16                res += sign * num
17                continue
18            elif c == "+":
19                sign = 1
20            elif c == "-":
21                sign = -1
22            elif c == "(":
23                stack.append((res, sign))
24                res, sign = 0, 1
25            elif c == ")":
26                prev_res, prev_sign = stack.pop()
27                res = prev_res + prev_sign * res
28            i += 1
29        
30        return res