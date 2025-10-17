# Last updated: 10/17/2025, 11:42:31 AM
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
