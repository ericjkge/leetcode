# Last updated: 6/5/2025, 5:47:06 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        mapping = {"2":"abc", 
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"}
        
        results = []

        def backtrack(index, path):
            if len(path) == len(digits):
                results.append("".join(path))
                return

            possible_letters = mapping[digits[index]]

            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        backtrack(0, [])
        return results



            
