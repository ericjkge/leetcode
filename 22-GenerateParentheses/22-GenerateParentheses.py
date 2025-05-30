# Last updated: 5/30/2025, 2:51:11 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, left, right):
            if len(curr) == 2 * n:
                ans.append("".join(curr))
                return
            if left < n:
                curr.append("(")
                backtrack(curr, left + 1, right)
                curr.pop()
            if right < left:
                curr.append(")")
                backtrack(curr, left, right + 1)
                curr.pop()
            
        ans = []
        backtrack([], 0, 0)
        return ans