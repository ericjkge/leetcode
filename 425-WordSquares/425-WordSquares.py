# Last updated: 9/4/2025, 10:42:15 AM
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        ans = []
        word_squares = []

        def backtrack(step):
            if step == n: # Start at index 0
                ans.append(word_squares[:])
                return
            
            prefix = "".join([word[step] for word in word_squares]) # Get prefix for current row
            for candidate in getWords(prefix):
                word_squares.append(candidate)
                backtrack(step + 1)
                word_squares.pop()
        
        def getWords(prefix):
            for word in words:
                if word.startswith(prefix):
                    yield word

        for word in words:
            word_squares = [word]
            backtrack(1)

        return ans