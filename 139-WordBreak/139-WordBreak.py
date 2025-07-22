# Last updated: 7/22/2025, 3:49:42 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        @cache
        def dp(i):
            if i == len(s):
                return True

            for word in wordSet:
                if s[i:i + len(word)] == word:
                    if dp(i + len(word)):
                        return True
            
            return False

        return dp(0)