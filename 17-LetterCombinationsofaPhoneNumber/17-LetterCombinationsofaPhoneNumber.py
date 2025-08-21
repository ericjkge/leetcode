# Last updated: 8/21/2025, 8:44:11 PM
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
        
        n = len(digits)
        ans = []
        
        if not digits:
            return []
        
        def backtrack(path, index):
            if index == n:
                ans.append("".join(path[:]))
                return
            
            for letter in mappings[digits[index]]:
                path.append(letter)
                backtrack(path, index + 1)
                path.pop()
        
        backtrack([], 0)
        return ans