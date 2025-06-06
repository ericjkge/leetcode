# Last updated: 6/6/2025, 1:27:35 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in mapping:
                if not stack or stack[-1] != mapping[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        if stack:
            return False
        return True