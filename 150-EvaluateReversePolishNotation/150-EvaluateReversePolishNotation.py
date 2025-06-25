# Last updated: 6/25/2025, 3:52:48 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        
        stack = []
        for token in tokens:
            if token not in operations.keys():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[token](a, b))
        return stack[0]
