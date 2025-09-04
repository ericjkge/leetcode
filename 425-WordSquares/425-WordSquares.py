# Last updated: 9/4/2025, 10:55:14 AM
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        ans, square = [], []

        prefixes = defaultdict(list)
        for word in words:
            for i in range(n + 1): # Include empty prefix
                prefixes[word[:i]].append(word)

        def backtrack(step):
            if step == n: # Start at index 0
                ans.append(square[:])
                return
            
            prefix = "".join([word[step] for word in square]) # Get prefix for current row
            for candidate in prefixes[prefix]:
                square.append(candidate)
                backtrack(step + 1)
                square.pop()
        
        for word in words:
            square = [word]
            backtrack(1)

        return ans