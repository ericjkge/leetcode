# Last updated: 5/30/2025, 12:08:05 PM
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
        
        ans = []
        def backtrack(index, path): # index is key to mapping
            if len(path) == len(digits):
                ans.append("".join(path))
                return
            
            letters = mapping[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        backtrack(0, [])
        return ans