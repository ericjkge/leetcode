# Last updated: 11/14/2025, 11:13:11 AM
class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {"(":")", "{":"}", "[":"]"}
        stack = []

        for c in s:
            if c in mappings:
                stack.append(c)
            else:
                if stack and mappings[stack.pop()] == c:
                    continue
                else:
                    return False
        
        return not stack