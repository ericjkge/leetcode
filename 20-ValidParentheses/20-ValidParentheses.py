# Last updated: 11/7/2025, 7:29:09 PM
class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {")":"(", "}":"{", "]":"["}

        stack = []
        for char in s:
            if char in mappings.values():
                stack.append(char)
            else:
                if stack and stack[-1] == mappings[char]:
                    stack.pop()
                else:
                    return False
        
        return not stack