# Last updated: 9/4/2025, 11:09:16 AM
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        prefixes = defaultdict(list)

        for word in words:
            for i in range(1, n + 1):
                prefixes[word[:i]].append(word)
        
        ans = []
        def backtrack(square, step):
            if step == n:
                ans.append(square[:])
                return 
            
            prefix = "".join(word[step] for word in square)
            for candidate in prefixes[prefix]:
                square.append(candidate)
                backtrack(square, step + 1)
                square.pop()

        for word in words:
            backtrack([word], 1)
        
        return ans