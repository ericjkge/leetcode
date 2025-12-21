# Last updated: 12/21/2025, 9:16:15 AM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        wordSet = set(wordDict)
4        n = len(s)
5
6        @cache
7        def dp(i):
8            if i == n:
9                return True
10
11            for word in wordSet:
12                if s[i:i + len(word)] == word:
13                    if dp(i + len(word)):
14                        return True
15            
16            return False
17
18        return dp(0)