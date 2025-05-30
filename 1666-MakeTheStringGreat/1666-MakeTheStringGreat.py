# Last updated: 5/30/2025, 12:07:26 PM
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in list(s):         
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
    
        return "".join(stack)