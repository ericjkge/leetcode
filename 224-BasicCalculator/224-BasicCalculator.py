# Last updated: 7/1/2025, 12:05:41 PM
class Solution:
    def calculate(self, s: str) -> int:
        ans, num, sign = 0, 0, 1
        stack = []
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                ans += (sign * num)
                if c == "+":
                    sign = 1
                if c == "-":
                    sign = -1
                num = 0
            elif c == "(":
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif c == ")":
                ans += (num * sign)
                ans *= stack.pop()
                ans += stack.pop()
                num = 0

        ans += (sign * num) # final number
        return ans

