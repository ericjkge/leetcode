# Last updated: 7/20/2026, 10:30:15 PM
1class Solution:
2    def calculate(self, s: str) -> int:
3        stack = []
4        num = 0
5        op = "+"
6
7        for i, c in enumerate(s):
8            if c.isdigit():
9                num = num * 10 + int(c)
10            if i == len(s) - 1 or c in "+-*/":
11                if op == "+":
12                    stack.append(num)
13                elif op == "-":
14                    stack.append(-num)
15                elif op == "*":
16                    stack.append(stack.pop() * num)
17                else:
18                    stack.append(int(stack.pop() / num))
19                op = c
20                num = 0
21        
22        return sum(stack)