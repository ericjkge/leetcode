# Last updated: 7/20/2025, 10:27:36 PM
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []

        def backtrack(path):
            if len(path) == n:
                ans.append(path[:])
                return
            
            for letter in ["a", "b", "c"]:
                if not path or path[-1] != letter:
                    path.append(letter)
                    backtrack(path)
                    path.pop()
            
        backtrack([])

        if len(ans) < k:
            return ""

        return "".join(ans[k - 1])