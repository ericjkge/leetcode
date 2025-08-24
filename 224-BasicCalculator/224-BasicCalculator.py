# Last updated: 8/24/2025, 10:50:54 AM
class Solution:
    def calculate(self, s: str) -> int:
        ans, num, sign = 0, 0, 1
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                ans += (sign * num) # Finish adding/subtracting prev number
                sign = 1 if c == "+" else -1
                num = 0
            elif c == "(":
                stack.append(ans)
                stack.append(sign)
                ans, sign = 0, 1
            elif c == ")":
                ans += (sign * num)
                prev_sign, prev_ans = stack.pop(), stack.pop()
                ans = prev_ans + (prev_sign * ans)
                num, sign = 0, 1
            else:
                continue # whitespace
        
        ans += (sign * num)
        return ans