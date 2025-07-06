# Last updated: 7/6/2025, 1:09:27 AM
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i!="*":
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)