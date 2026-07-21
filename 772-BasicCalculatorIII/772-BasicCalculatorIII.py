# Last updated: 7/20/2026, 10:58:38 PM
1class Solution:
2    def calculate(self, s: str) -> int:
3        def helper(i):
4            stack = []
5            num = 0
6            op = "+"
7
8            while i < len(s):
9                c = s[i]
10                if c.isdigit():
11                    num = num * 10 + int(c)
12                elif c == "(":
13                    num, i = helper(i + 1)
14                if c in "+-*/)" or i == len(s) - 1:
15                    if op == "+":
16                        stack.append(num)
17                    elif op == "-":
18                        stack.append(-num)
19                    elif op == "*":
20                        stack.append(stack.pop() * num)
21                    elif op == "/":
22                        stack.append(int(stack.pop() / num))
23                    op = c
24                    num = 0
25                    if c == ")":
26                        return sum(stack), i
27                i += 1
28            return sum(stack), i
29
30        return helper(0)[0]