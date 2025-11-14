# Last updated: 11/14/2025, 11:13:48 AM
class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {"(":")", "{":"}", "[":"]"}
        stack = []

        for c in s:
            if c in mappings:
                stack.append(c)
            else:
                if not stack or mappings[stack.pop()] != c:
                    return False
        
        return not stack