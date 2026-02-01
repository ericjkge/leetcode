# Last updated: 2/1/2026, 3:18:28 PM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        operations = {
4           "+": lambda a, b: a + b,
5           "-": lambda a, b: a - b,
6           "*": lambda a, b: a * b,
7           "/": lambda a, b: int(a / b)
8        }
9
10        stack = []
11        for token in tokens:
12            if token in operations:
13                b, a = stack.pop(), stack.pop()
14                res = operations[token](a, b)
15                stack.append(res)
16            else:
17                stack.append(int(token))
18        
19        return stack[0]
20
21class Solution:
22    def evalRPN(self, tokens: List[str]) -> int:
23        stack = []
24        mappings = {
25            "+": lambda x, y: x + y,
26            "-": lambda x, y: x - y,
27            "*": lambda x, y: x * y,
28            "/": lambda x, y: int(x / y)
29        }
30
31        for token in tokens:
32            if token in mappings:
33                y, x = stack.pop(), stack.pop()
34                stack.append(mappings[token](x, y))
35            else:
36                stack.append(int(token))
37        
38        return stack[0]