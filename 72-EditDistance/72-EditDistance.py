# Last updated: 11/22/2025, 2:26:14 PM
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a, b = len(word1), len(word2)

        @cache
        def dp(i, j):
            if i == a and j == b:
                return 0
            
            if i == a:
                return len(word2[j:]) # same as b - j
            
            if j == b:
                return len(word1[i:])

            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)

            return 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))
        
        return dp(0, 0)