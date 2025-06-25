# Last updated: 6/25/2025, 1:11:45 PM
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

        if digits == "":
            return []

        ans = []
        def backtrack(index, path):
            if len(path) == len(digits):
                ans.append("".join(path))
                return
            
            possible_letters = mapping[digits[index]]

            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return ans