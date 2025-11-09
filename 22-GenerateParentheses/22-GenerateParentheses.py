# Last updated: 11/8/2025, 8:50:12 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(open, closed, path):
            if len(path) == 2 * n:
                ans.append("".join(path))
                return
            
            if open < n:
                path.append("(")
                backtrack(open + 1, closed, path)
                path.pop()

            if closed < open:
                path.append(")")
                backtrack(open, closed + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return ans