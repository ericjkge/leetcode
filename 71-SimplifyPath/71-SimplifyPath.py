# Last updated: 5/30/2025, 12:08:03 PM
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        split_path = path.split("/")

        stack = []
        for portion in split_path:
            if portion == "." or not portion:
                pass
            elif portion == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(portion)
        
        return "/" + "/".join(stack)
    