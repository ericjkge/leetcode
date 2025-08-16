# Last updated: 8/16/2025, 10:14:02 AM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        if not digits:
            return []

        ans = []
        def backtrack(path, index):
            if index == len(digits):
                ans.append("".join(path))
                return

            for letter in mapping[digits[index]]:
                path.append(letter)
                backtrack(path, index + 1)
                path.pop()
        
        backtrack([], 0)
        return ans