# Last updated: 11/7/2025, 6:56:12 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        def backtrack(index, path):
            if len(path) == len(digits):
                ans.append("".join(path))
                return
            
            for letter in mappings[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
                
        backtrack(0, [])
        return ans