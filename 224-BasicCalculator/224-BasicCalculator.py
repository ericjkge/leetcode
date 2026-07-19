# Last updated: 7/19/2026, 10:39:34 AM
1class Solution:
2    def calculate(self, s: str) -> int:
3        stack = []
4        num = 0
5        sign = 1
6        total = 0
7
8        for ch in s:
9            if ch.isdigit():
10                num *= 10
11                num += int(ch)
12            elif ch == "(":
13                stack.append(sign)
14                stack.append("(")
15                sign = 1
16            elif ch == ")":
17                stack.append(sign * num)
18                num = 0
19                while stack[-1] != "(":
20                    num += stack.pop()
21                stack.pop()
22                num *= stack.pop()
23                sign = 1
24            elif ch == "+":
25                stack.append(sign * num)
26                num = 0
27                sign = 1
28            elif ch == "-":
29                stack.append(sign * num)
30                num = 0
31                sign = -1
32            else:
33                continue
34
35        stack.append(sign * num)
36        while stack:
37            total += stack.pop()
38        
39        return total