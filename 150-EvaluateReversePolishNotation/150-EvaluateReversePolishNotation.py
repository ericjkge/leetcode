# Last updated: 12/22/2025, 7:05:10 PM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        operations = {
4           "+": lambda a, b: a + b,
5           "-": lambda a, b: a - b,
6           "*": lambda a, b: a * b,
7           "/": lambda a, b: a / b 
8        }
9
10        stack = []
11        for token in tokens:
12            if token in operations:
13                b, a = int(stack.pop()), int(stack.pop())
14                res = operations[token](a, b)
15                stack.append(res)
16            else:
17                stack.append(token)
18        
19        return int(stack[0])