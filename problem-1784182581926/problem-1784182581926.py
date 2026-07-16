# Last updated: 7/15/2026, 11:16:21 PM
1class Solution:
2    def diffWaysToCompute(self, expression: str) -> List[int]:
3        operations = {
4            "+": lambda x, y: x + y,
5            "-": lambda x, y: x - y,
6            "*": lambda x, y: x * y
7        }
8
9        @cache
10        def dp(exp):
11            if exp.isdigit():
12                return [int(exp)]
13            
14            res = []
15            for i, ch in enumerate(exp):
16                if ch in operations:
17                    left = dp(exp[:i])
18                    right = dp(exp[i + 1:])
19
20                    for a in left:
21                        for b in right:
22                            res.append(operations[ch](a, b))
23
24            return res
25        
26        return dp(expression)
27            