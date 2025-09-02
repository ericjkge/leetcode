# Last updated: 9/1/2025, 8:24:45 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        mappings = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        ans = []
        n = len(digits)

        def backtrack(path, index):
            if index == n:
                ans.append("".join(path))
                return
            
            for c in mappings[digits[index]]:
                path.append(c)
                backtrack(path, index + 1)
                path.pop()

        backtrack([], 0)
        return ans