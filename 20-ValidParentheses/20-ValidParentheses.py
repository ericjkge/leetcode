# Last updated: 6/24/2025, 5:19:24 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(":")", "{":"}", "[":"]"}

        for char in s:
            if char in mapping.keys():
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char != mapping[stack.pop()]:
                    return False
        
        return not stack
