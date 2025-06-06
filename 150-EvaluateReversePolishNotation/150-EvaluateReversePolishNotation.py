# Last updated: 6/6/2025, 3:13:43 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+" : lambda a, b: a + b, 
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: int(a / b),
        }

        stack = []
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[token](a, b))

        return stack.pop()