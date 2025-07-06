# Last updated: 7/6/2025, 1:09:12 AM
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "*":
                stack.pop()
            else:
                stack.append(s[i])
        
        return "".join(stack)